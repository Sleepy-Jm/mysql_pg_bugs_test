"""Copied lexical parsers only; no legacy oracle or target matrix."""
import re

def split_sql(text):
    """Split these simple SQL scripts; retain physical line ranges for client errors."""
    statements, buf = [], []
    quote = None
    block = False
    line = 1
    start = None
    i = 0
    while i < len(text):
        char = text[i]
        pair = text[i:i + 2]
        if block:
            if pair == '*/':
                block = False
                buf.append(' ')
                i += 2
                continue
            if char == '\n':
                line += 1
            i += 1
            continue
        if quote:
            buf.append(char)
            if char == '\n':
                line += 1
            if char == '\\' and i + 1 < len(text):
                buf.append(text[i + 1])
                line += text[i + 1] == '\n'
                i += 2
                continue
            if char == quote:
                if i + 1 < len(text) and text[i + 1] == quote:
                    buf.append(text[i + 1])
                    i += 2
                    continue
                quote = None
            i += 1
            continue
        if char == '#' or (pair == '--' and (i + 2 == len(text) or text[i + 2].isspace())):
            end = text.find('\n', i)
            if end < 0:
                break
            buf.append('\n')
            line += 1
            i = end + 1
            continue
        if pair == '/*':
            block = True
            i += 2
            continue
        if char == ';':
            if ''.join(buf).strip():
                sql = ''.join(buf).strip()
                statements.append({'sql': sql, 'line_start': start, 'line_end': line,
                                   'normalized': normalize_sql(sql)})
            buf, start = [], None
            i += 1
            continue
        if start is None and not char.isspace():
            start = line
        if char in "'\"`":
            quote = char
        buf.append(char)
        if char == '\n':
            line += 1
        i += 1
    if quote or block:
        raise ValueError('Unterminated quoted SQL or block comment')
    if ''.join(buf).strip():
        sql = ''.join(buf).strip()
        statements.append({'sql': sql, 'line_start': start, 'line_end': line, 'normalized': normalize_sql(sql)})
    return statements


def normalize_sql(sql):
    # All compared literals in this frozen batch are simple ASCII; case folding
    # is used only to align the echoed statement with the exact executed script.
    return re.sub(r'\s+', ' ', sql.strip().rstrip(';')).casefold()


def parse_verbose(stdout):
    delimiters = list(re.finditer(r'(?m)^--------------\r?$', stdout))
    if not delimiters or len(delimiters) % 2:
        raise ValueError('Missing or incomplete mysql verbose statement boundaries')
    if stdout[:delimiters[0].start()].strip():
        raise ValueError('Unclassified output before first SQL boundary')
    segments = []
    for n in range(0, len(delimiters), 2):
        query = stdout[delimiters[n].end():delimiters[n + 1].start()].strip()
        statements = split_sql(query)
        if len(statements) != 1:
            raise ValueError('Verbose SQL block is not one statement')
        end = delimiters[n + 2].start() if n + 2 < len(delimiters) else len(stdout)
        body = stdout[delimiters[n + 1].end():end].strip('\r\n')
        # -v usually omits status prose; accepting explicit standard status lines
        # also makes transcripts from otherwise identical clients auditable.
        lines = [s.rstrip('\r') for s in body.split('\n') if s.strip()]
        lines = [s for s in lines if not re.match(r'^(?:Query OK,|Empty set(?:\s|$)|\d+ rows? in set\b|Bye$)', s)]
        header = lines[0].split('\t') if lines else []
        rows = [s.split('\t') for s in lines[1:]] if lines else []
        segments.append({'sql': statements[0]['sql'], 'normalized': statements[0]['normalized'],
                         'header': header, 'rows': rows, 'raw_body': body,
                         'shape_valid': all(len(row) == len(header) for row in rows)})
    return segments


def parse_errors(stderr, statements):
    errors = []
    starts = list(re.finditer(r'(?m)^ERROR\s+(\d+)(?:\s+\(([^)]+)\))?(?:\s+at line\s+(\d+))?\s*:', stderr))
    for n, match in enumerate(starts):
        line = int(match[3]) if match[3] else None
        message = stderr[match.end():starts[n + 1].start() if n + 1 < len(starts) else len(stderr)].strip()
        indices = [i for i, statement in enumerate(statements) if line is not None and statement['line_start'] <= line <= statement['line_end']]
        errors.append({'code': int(match[1]), 'sqlstate': match[2], 'line': line,
                       'statement_index': indices[0] if len(indices) == 1 else None, 'message': message})
    unparsed = [s for s in stderr.splitlines() if re.match(r'^ERROR\b', s) and not any(s.startswith(m[0]) for m in starts)]
    return errors, unparsed
