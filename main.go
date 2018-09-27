package main

//golang 操作selenium浏览器
//QQ:29295842  希望大家多多来交流
import (
	//"admin"
	"fmt"
	//	"log"
	//log "fmt"
	"Chrome"
	//"g"
	"github.com/tebeka/selenium"
)

func main() {
	//fmt.Printf("===%v===\n", selenium.BackspaceKey)
	Chrome.Chrome_close_ie() //结束浏览器
	//==============================
	fmt.Println("百度点击搜索")
	Chrome.Chrome_ini()                                                                                                    //初始化配置
	Chrome.Chrome_add_argument("--user-agent", "--user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36") //更改配置
	Chrome.Chrome_open()
	Chrome.Chrome_get("https://www.baidu.com/") //打开浏览器
	//Chrome.Chrome_switch_to_frame("id", "kw", "")  //定位错误
	Chrome.Chrome_send_keys("id", "kw", "1234567890", "1") //发送指令
	Chrome.Chrome_click("id", "su", "")                    //点击动作

	Chrome.Chrome_send_keys("id", "kw", Chrome.Chrome_Keys_data("BACKSPACE"), "1") //发送指令
	Chrome.Chrome_send_keys("id", "kw", Chrome.Chrome_Keys_data("BACKSPACE"), "1") //发送指令
	Chrome.Chrome_send_keys("id", "kw", Chrome.Chrome_Keys_data("BACKSPACE"), "1") //发送指令

	//==============================

}
