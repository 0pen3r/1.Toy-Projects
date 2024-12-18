Set ws = CeateObject("WScript.Shell")
Do
  WScript.Sleep 59000
  ws.Sendkeys "{CAPSLOCK}{CAPSLOCK}"
Loop


'vbs 파일의 주석은 ' 이다
'59초마다 캡락 2번 입력한다.
