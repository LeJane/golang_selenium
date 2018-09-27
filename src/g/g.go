package g

import (
	"fmt"
	"os/exec"
	"strings"

	"github.com/axgle/mahonia"
)

var (
	Dbug_log = true //调试状态
)

//=====================================
func Panic_Err() {
	if err := recover(); err != nil {
		if Dbug_log == true {
			fmt.Printf("=err===%v===\n", err)
		} else {
			//写入日志

		}
		//fmt.Println(err) //这里的err其实就是panic传入的内容，55
	}
}

func Cmdexec(cmd string, system string) string {
	defer Panic_Err() //异常处理
	var c *exec.Cmd
	var data string
	if system == "windows" {
		argArray := strings.Split("/c "+cmd, " ")
		c = exec.Command("cmd", argArray...)
	} else {
		c = exec.Command("/bin/sh", "-c", cmd)
	}
	out, _ := c.Output()
	data = string(out)
	if system == "windows" {
		dec := mahonia.NewDecoder("gbk")
		data = dec.ConvertString(data)
	}
	return data
}
