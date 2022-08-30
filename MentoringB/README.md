```bash
# build docker image
git clone -b week_7 --single-branch https://github.com/BOAZ-bigdata/19Engineering_BASE
```

```bash
# upload docker container
docker build -t boaz19-efk-source:{{ tag }}
docker tag boaz19-efk-source:{{ tag }} {{ docker username }}/boaz19-efk-source:{{ tag }}
sudo docker push {{ docker username }}/boaz19-efk-source:{{ tag }}
```
