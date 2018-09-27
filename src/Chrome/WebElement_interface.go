package Chrome

//QQ:29295842  希望大家多多来交流
import (
	"fmt"
	//	"log"

	//	"github.com/tebeka/selenium"
	//	"github.com/tebeka/selenium/chrome"
	//	"os/exec"
	//	"strings"
	//	"g"
	//"reflect"
	//	"errors"
	//"strconv"
	//	"strings"
	//	"github.com/axgle/mahonia"
)

//===================================================================
func Chrome_send_keys(fx, name, key, id string) bool { //发送文字操作
	Element, err := FindElement(fx, name, id)
	if err != nil {
		return false
	}
	if err = Element.SendKeys(key); err != nil {
		return false
	}
	return true
}

func Chrome_click(fx, name, id string) bool { //点击操作
	Element, err := FindElement(fx, name, id)
	if err != nil {
		return false
	}
	if err = Element.Click(); err != nil {
		return false
	}
	return true
}

func Chrome_clear(fx, name, id string) bool { //清空文本
	Element, err := FindElement(fx, name, id)
	if err != nil {
		return false
	}
	if err = Element.Clear(); err != nil {
		return false
	}
	return true
}

func Chrome_submit(fx, name, id string) bool { //提交表单
	Element, err := FindElement(fx, name, id)
	if err != nil {
		return false
	}
	if err = Element.Submit(); err != nil {
		return false
	}
	return true
}

func Chrome_size(fx, name, id string) (string, bool) { //文件大小  返回元素的大小。
	Element, err := FindElement(fx, name, id)
	if err != nil {
		return "", false
	}
	Size, err := Element.Size()
	if err != nil {
		return "", false
	}
	return fmt.Sprintf("%v", Size.Width*Size.Height), true
}

func Chrome_text(fx, name, id string) (string, bool) { //获取内容
	Element, err := FindElement(fx, name, id)
	if err != nil {
		return "", false
	}
	Text, err := Element.Text()
	if err != nil {
		return "", false
	}
	return fmt.Sprintf("%v", Text), true
}

//==Click() error
//==SendKeys(keys string) error
//==Submit() error
//==Clear() error
//==Size() (*Size, error)
//==Text() (string, error)
//=======================================
//	// MoveTo moves the mouse to relative coordinates from center of element, If===MoveTo将鼠标从元素中心移动到相对坐标，如果
//	// the element is not visible, it will be scrolled into view.===元素是不可见的，它将被滚动到视图中。
//	MoveTo(xOffset, yOffset int) error
//	// FindElement finds a child element. ===FieldEnter发现子元素。
//	FindElement(by, value string) (WebElement, error)
//	// FindElement finds multiple children elements.===FieldEnter发现多个子元素。
//	FindElements(by, value string) ([]WebElement, error)
//	// TagName returns the element's name.===TAGNEY返回元素的名称。
//	TagName() (string, error)
//	// IsSelected returns true if element is selected.===如果选择元素，ISOSET返回true。
//	IsSelected() (bool, error)
//	// IsEnabled returns true if the element is enabled.===如果启用了元素，ISFAID返回true。
//	IsEnabled() (bool, error)
//	// IsDisplayed returns true if the element is displayed.===如果显示元素，则ISDISTIFY返回true。
//	IsDisplayed() (bool, error)
//	// GetAttribute returns the named attribute of the element.===返回元素的命名属性。
//	GetAttribute(name string) (string, error)
//	// Location returns the element's location.===位置返回元素的位置。
//	Location() (*Point, error)
//	// LocationInView returns the element's location once it has been scrolled===LooCurnVIEW在元素滚动后返回元素的位置。
//	// into view.===进入/查看。
//	LocationInView() (*Point, error)
//	// CSSProperty returns the value of the specified CSS property of the===CSStand返回指定的CSS属性的值
//	// element.===元素。
//	CSSProperty(name string) (string, error)

//===================================================================
