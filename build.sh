# to build on my m4 mac

docker buildx build --tag genepattern/tfsites:15.9 -f Dockerfile_incremental -o type=image --platform=linux/amd64,linux/arm64 --push  .

