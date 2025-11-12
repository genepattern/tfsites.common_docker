# to build on my m4 mac

docker buildx build --tag genepattern/tfsites:17.1.3 -f Dockerfile -o type=image --platform=linux/amd64 --push  .

