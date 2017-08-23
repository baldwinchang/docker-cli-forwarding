# docker-cli-forwarding
Simple request forwarder for the docker-cli that you can service link other containers with. This is primarily useful for dynamic Nvidia volume mounting.

By default, this container runs on port 411.

## Run this image

```
docker run -net=host -d baldwinchang/docker-cli-forwarding
```