# sistech


# command

알파채널이 적용된 `tif` 파일에서 이미지가 있는 부위를 픽셀단위로 줄여내는 커멘드

`--debug True` 옵션을 넣는다면 삭제된 부위를 빨간색으로 처리한다.
`--pixel_width 40` 40 pixel 을 자른다. 기본값이나 없다면 10 pixel 

```
 ./reduce_tif.py ./tests/fixture/학동리-8384.tif /mnt/d/systech-output/trans/test1.tif --pixel_width 40 --debug True
```
