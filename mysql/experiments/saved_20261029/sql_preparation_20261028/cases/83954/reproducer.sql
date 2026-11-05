-- MySQL report #83954; source anchors: cmain, c535693, c542289
-- Static preparation only; not executed. Use a fresh isolated schema/instance as specified in case.json.
SELECT 
@j0 := JSON_OBJECT('a',123456789012345678901234567890) json_object_,
CAST(CAST(JSON_OBJECT('a',123456789012345678901234567890) AS CHAR) AS JSON) json_object_from_char_,
CAST(@j0 AS JSON) json_object_from_variable_,
JSON_EXTRACT(JSON_OBJECT('a',123456789012345678901234567890),'$.a') json_value_,
JSON_EXTRACT(@j0,'$.a') json_value_from_variable;
