### traefik redis 服务发现配置

#### server run

`traefik --api.insecure=True --providers.redis.endpoints=127.0.0.1:6379 --providers.redis.rootkey=traefik --log --log.level=DEBUG`

#### redis 配置

1. **Add Route** (我们例子中router `lmy`)

   ``set traefik/http/routers/lmy/rule  Host(`lmy.local`)``

   

2. **Add Service**

   `set traefik/http/routers/lmy/service lmyservice`

   

3. **Add backend**

   `set traefik/http/services/lmyservice/loadBalancer/servers/0/url http://backend1`

   `set traefik/http/services/lmyservice/loadBalancer/servers/1/url http://backend2`

   **在完成上述操作就实现redis 服务发现**

   

4. **服务检测**
   `set traefik/http/services/lmyservice/loadBalancer/healthCheck/interval 5`
   `set traefik/http/services/lmyservice/loadBalancer/healthCheck/path /`

   
   
5. **添加白名单**

   `set traefik/http/routers/lmyservice/middlewares/0 lmymd`

   `set traefik/http/middlewares/lmymd/ipWhiteList/sourceRange/0 192.168.0.1`

   

6.  **如果后续我们要+其他middleware 可以参考（比如限流）**

    [KV Configuration Reference](https://docs.traefik.io/reference/dynamic-configuration/kv/)

