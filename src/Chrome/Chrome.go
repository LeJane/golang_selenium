package Chrome

//QQ:29295842  希望大家多多来交流
import (
	"fmt"
	//	"log"

	"github.com/tebeka/selenium"
	"github.com/tebeka/selenium/chrome"
	//	"os/exec"
	//	"strings"
	//	"g"
	//"reflect"
	//	"errors"
	//"strconv"
	"strings"
	//	"github.com/axgle/mahonia"
)

//Chrome_add_argument("--user-agent","--user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36")  //更改配置
func Chrome_add_argument(key, data string) bool { //更换头部
	var bj = false
	for k, v := range argss {
		if strings.Contains(v, key) {
			bj = true
			argss[k] = data
			break //#跳出
		}
	}
	if bj == false {
		bj = true
		argss = append(argss, data)
	}
	return bj
}

func Chrome_init() { //初始化
	chromeCaps := chrome.Capabilities{
		Prefs: imagCaps,
		Path:  "",
		Args:  argss,
	}
	caps.AddChrome(chromeCaps)
}

func Chrome_open() bool { //打开浏览器
	Chrome_init() //初始化
	opts := []selenium.ServiceOption{}
	// 启动chromedriver，端口号可自定义
	//service, err = selenium.NewChromeDriverService("/opt/google/chrome/chromedriver", 9515, opts...)
	_, err := selenium.NewChromeDriverService("Chrome/chromedriver.exe", 9515, opts...)
	if err != nil {
		//log.Printf("Error starting the ChromeDriver server: %v", err)
		return false
	}
	// 调起chrome浏览器WebDriver
	Browser, err = selenium.NewRemote(caps, fmt.Sprintf("http://localhost:%d/wd/hub", 9515))
	if err != nil {
		//panic(err)
		return false
	}
	Browser.MaximizeWindow("") //最大化浏览器
	return true
	//fmt.Printf("=err===%v===\n", webDriver.(type))
	// 导航到目标网站
	//	err = Browser.Get("http://baidu.com")
	//	if err != nil {
	//		panic(fmt.Sprintf("Failed to load page: %s\n", err))
	//	}
	//	log.Println(Browser.Title())
}

//===================================================================

//===================================================================
