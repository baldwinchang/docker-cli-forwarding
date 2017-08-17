# docker-cli-forwarding
Simple request forwarder for the docker-cli that you can service link other containers with. This is primarily useful for dynamic Nvidia volume mounting.

## Run this image

```
export APP_PORT=5000
docker run -net=host -p $APP_PORT:$APP_PORT -d baldwinchang/docker-cli-forwarding
```