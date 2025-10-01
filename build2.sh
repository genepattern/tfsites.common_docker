# to build on my m4 mac

docker buildx build --tag genepattern/tfsites:17.0.2.1 -f Dockerfile -o type=image --platform=ilinux/arm64 --push  .

