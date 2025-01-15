# to build on my m4 mac

docker buildx build --tag genepattern/tfsites:0.13 -o type=image --platform=linux/arm64,linux/amd64 --push  .

