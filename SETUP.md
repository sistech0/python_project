
## 기본 환경 설정
### 개발 및 전처리 환경
- nvidia GPU 가 있는 윈도우즈 11 노트북
- 리눅스 셋업을 위해서 WSL2 로 세팅하여야함
- nvidia GPU driver를 최신으로 업데이트가 필요함
  - [가이드라인](https://docs.nvidia.com/cuda/wsl-user-guide/index.html)
  - [드라이버 - 윈도우용](https://developer.nvidia.com/cuda/wsl)
  - 윈도우에 드라이버를 설치하고 리눅스에 다시 드라이버를 세팅해야함
  - WSL2에서 환경 구축후에 python 에서 tensorflow 가 제대로 설치되었는지 확인이 필요함 . 아래의 구문을 쳤을때 True가 반환되어야함
  ```
  import tensorflow as tf
  tf.test.is_gpu_available
  ```
- `nvidia-smi` 명렁어를 통하여 설치된 드라이버등의 정보를 확인이 가능하다.
```
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 470.82.01    Driver Version: 472.56       CUDA Version: 11.4     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  NVIDIA GeForce ...  Off  | 00000000:01:00.0  On |                  N/A |
| N/A   43C    P8    11W /  N/A |    466MiB /  6144MiB |    ERR!      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
```

#### pyenv 설치

[설치가이드참조](https://jinmay.github.io/2019/03/16/linux/ubuntu-install-pyenv-1/)

### pirtualenv 만들고 패키지 설치
pyenv 설치후에 파이썬 3.9.10를 설치하고 virtualenv 를 만들어야한다.

```
pyenv install 3.9.10
pyenv virtualenv 3.9.10 sistech
```

github 로긴을 위해서 github cli 를 설치한다.
[설치가이드](https://github.com/cli/cli/blob/trunk/docs/install_linux.md#debian-ubuntu-linux-raspberry-pi-os-apt)

```
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/etc/apt/trusted.gpg.d/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/trusted.gpg.d/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

설치된 이후에 github 로긴을 cli 에서 진행한다. 아래를 실행하고 토큰을 복사후에 브라우저에서 인증한다.

```
gh login auth
```


repository 를 복제하고 해당 디렉토리에 들어가서 해당 디렉토리를 local 디렉토리로 만들고 패키지를 설치한다.
```
git clone https://github.com/hyeonhwana/sistech.git
cd sistech
pyenv local sistech
pip install -r --upgrade requirements.txt
```
### NAS 마운트
`root` 로 패키지 설치

```
apt-get install davfs2
mkdir -p /home/user/nas
chown user /home/user/nas
```

/home/user/nas 디렉토리에 nas 마운트 


```
mount -t davfs -o uid=1000  https://sistech3.synology.me:32220/Ai_work /home/user/nas

```

작업이 끝난후에 unmount 는 `root` 로 다음과 같이 한다.
```
umount /home/dj/nas
```


### 파일 전처리

T.B.D

### 코랩으로 데이터 복제

T.B.D


### 코랩에서 NAS 마운트
/content/nas 디렉토리를 만들고 nas 를 마운트한다.

```
mkdir /content/nas 
mount -t davfs  https://sistech3.synology.me:32220/Ai_work /content/nas 
```


### 코랩에서 모델링 NAS 로 업로드

T.B.D


### 로컬에서 모델링 로드해서 테스팅


T.B.D

