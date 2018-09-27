package Chrome

//QQ:29295842  希望大家多多来交流
import (
	"fmt"
	//	"log"

	"github.com/tebeka/selenium"
	//	"github.com/tebeka/selenium/chrome"
	//	"os/exec"
	//	"strings"
	"g"
	//"reflect"
	"errors"
	"strconv"
	//	"strings"
	//	"github.com/axgle/mahonia"
)

var (
	Browser  selenium.WebDriver
	caps     = selenium.Capabilities{}
	argss    = []string{} // 设置Chrome模式
	imagCaps = map[string]interface{}{}
)

//自定义的出错结构
type myError struct {
	arg    int
	errMsg string
}

//实现Error接口
func (e *myError) Error() string {
	return fmt.Sprintf("%d - %s", e.arg, e.errMsg)
}

func Chrome_close_ie() { //结束浏览器
	defer g.Panic_Err() //异常处理
	g.Cmdexec("taskkill /im chrome.exe /f", "windows")
	g.Cmdexec("taskkill /im chromedriver.exe /f", "windows")
	//	Public_file.Cmdexec("taskkill /f /t /im main.exe", "windows")
	//	cmd := `.\\ie\\main.exe` //taskkill /f /t /im main.exe
	//	argArray := strings.Split("/c "+cmd, " ")
	//	c := exec.Command("cmd", argArray...)
	//	//out, err :=
	//	c.Output()
	//fmt.Printf("==%v=====%v====\n", err, string(out))
}

func Chrome_ini() { //初始化配置
	// 禁止加载图片，加快渲染速度
	imagCaps = map[string]interface{}{
	//"profile.managed_default_content_settings.images": 2,   // 禁止加载图片
	//{"--disable-bundled-ppapi-flash": 2}    //禁止FLSH
	}
	caps = selenium.Capabilities{
		"browserName": "chrome",
	}
	argss = []string{ //"--headless", // 设置Chrome无头模式
		//"--no-sandbox",
		"--disable-infobars",
		"--disable-bundled-ppapi-flash", //禁止加载FLSH
		"--disable-internal-flash",      //禁止加载FLSH
		"--disable-flash-core-animation",
		// user-agent，	头
		"--user-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
	}
}

func FindElement(fx, name, id string) (selenium.WebElement, error) {
	if id == "" {
		Element, err := Browser.FindElement(fx, name) //[int(id)]
		if err != nil {
			return nil, err
		}
		return Element, err
	} else {
		Element, err := Browser.FindElements(fx, name)
		if err != nil {
			return nil, err
		}
		i, err := strconv.Atoi(id)
		if err != nil {
			return nil, err
		}
		if len(Element) <= i {
			return Element[i-1], err
		}
	}
	return nil, errors.New("FindElement err!")
}
