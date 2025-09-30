# to build on my m4 mac

docker buildx build --tag genepattern/tfsites:17.0.2 -f Dockerfile -o type=image --platform=linux/amd64 --push  .

