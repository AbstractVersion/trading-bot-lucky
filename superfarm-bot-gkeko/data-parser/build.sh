echo 'Building parser image for pv-adapt energy measurments retrieval.'
cd app-cron && docker image build -t private.registry.io/data-parser-superfarm:ftnsecs .
# docker image push private.registry.io/data-parser-pvadapt:latest