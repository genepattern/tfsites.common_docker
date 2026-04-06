# to build on my m4 mac

docker buildx build --tag genepattern/tfsites:18.0 -f Dockerfile -o type=image --platform=linux/amd64 --push  .

