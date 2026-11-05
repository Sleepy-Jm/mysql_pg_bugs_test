concurrency=2
output=/tmp/junk
rm -rf $output
printf "$(printf "test: two-ids\n%.0s" `seq 100`)"
>/tmp/isolation_schedule
for c in `seq $concurrency`; do
mkdir -p $output/results_${c}
(EXTRA_REGRESS_OPTS="--dbname=regress_${c} --outputdir=$output/results_${c}
--schedule=/tmp/isolation_schedule" make -C src/test/isolation installcheck)
\
        > $output/out.${c}.log 2>&1 &
done
wait
coredumpctl --no-pager;
