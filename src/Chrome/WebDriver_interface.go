package Chrome

//QQ:29295842  希望大家多多来交流
import (
	"fmt"
	//	"log"

	"github.com/tebeka/selenium"
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
func Chrome_get(url string) bool { //打开浏览器
	//	Browser.AddCookie(&selenium.Cookie{
	//		Name:  "defaultJumpDomain",
	//		Value: "www",
	//	})
	if err := Browser.Get(url); err != nil {
		return false
	}
	return true
}

//=============
func Chrome_max_window() bool { //最大化浏览器
	if err := Browser.MaximizeWindow(""); err != nil {
		return false
	}
	return true
}

func Chrome_page_forward() bool { //浏览器页面前进
	if err := Browser.Forward(); err != nil {
		return false
	}
	return true
}

func Chrome_page_back() bool { //浏览器页面后退
	if err := Browser.Back(); err != nil {
		return false
	}
	return true
}

func Chrome_page_refresh() bool { //浏览器页面刷新
	if err := Browser.Refresh(); err != nil {
		return false
	}
	return true
}

//=============

func Chrome_get_title() (string, bool) { //获取页面标题
	Title, err := Browser.Title()
	if err != nil {
		return "", false
	}
	return fmt.Sprintf("%v", Title), true
}

func Chrome_add_cookie(name, value string) bool { //设置cookie
	err := Browser.AddCookie(&selenium.Cookie{
		Name:  name,
		Value: value,
	})
	if err != nil {
		return false
	}
	return true
}

//===================================================================
//==Get(url string) error
//==MaximizeWindow(name string) error
//==Forward() error
//==Back() error
//==Refresh() error
//==Title() (string, error)
//==AddCookie(cookie *Cookie) error
//==================

//	// Status returns various pieces of information about the server environment.===状态返回有关服务器环境的各种信息。
//	Status() (*Status, error)
//	// NewSession starts a new session and returns the session ID.===NeXession启动一个新的会话并返回会话ID。
//	NewSession() (string, error)
//	// SessionId returns the current session ID===SeSession ID返回当前会话ID
//	// Deprecated: This identifier is not Go-style correct. Use SessionID===不推荐：这个标识符不正确。使用Session ID
//	// instead.    相反。
//	SessionId() string
//	// SessionID returns the current session ID. ===SeSession ID返回当前会话ID。
//	SessionID() string
//	// SwitchSession switches to the given session ID.===切换会话切换到给定会话ID.
//	SwitchSession(sessionID string) error
//	// Capabilities returns the current session's capabilities.===能力返回当前会话的能力。
//	Capabilities() (Capabilities, error)
//	// SetAsyncScriptTimeout sets the amount of time that asynchronous scripts===StasyNyScript TimeOutt设置异步脚本的时间量
//	// are permitted to run before they are aborted. The timeout will be rounded===允许在被中止之前运行。超时将被舍入。
//	// to nearest millisecond.===接近最近毫秒。
//	SetAsyncScriptTimeout(timeout time.Duration) error
//	// SetImplicitWaitTimeout sets the amount of time the driver should wait when===SimTimPrimeWaITTimeOutt设置驱动程序等待的时间量
//	// searching for elements. The timeout will be rounded to nearest millisecond.===搜索元素。超时将被舍入到最近毫秒。
//	SetImplicitWaitTimeout(timeout time.Duration) error
//	// SetPageLoadTimeout sets the amount of time the driver should wait when===StPaPeloOdTimeUT设置驱动程序应该等待的时间量
//	// loading a page. The timeout will be rounded to nearest millisecond.===加载页面。超时将被舍入到最近毫秒。
//	SetPageLoadTimeout(timeout time.Duration) error
//	// Quit ends the current session. The browser instance will be closed. ===退出当前会话结束。浏览器实例将被关闭。
//	Quit() error
//	// CurrentWindowHandle returns the ID of current window handle. ===CurrentWindowHandle返回当前窗口句柄的ID。
//	CurrentWindowHandle() (string, error)
//	// WindowHandles returns the IDs of current open windows. ===Windows句柄返回当前打开的窗口的ID。
//	WindowHandles() ([]string, error)
//	// CurrentURL returns the browser's current URL. ===CurrutURL返回浏览器的当前URL。
//	CurrentURL() (string, error)
//	// Title returns the current page's title. ===标题返回当前页的标题。
//	Title() (string, error)
//	// PageSource returns the current page's source.===PageSource返回当前页面的源代码。
//	PageSource() (string, error)
//	// Close closes the current window. ===关闭当前窗口。
//	Close() error
//	// SwitchFrame switches to the given frame. The frame parameter can be the===交换帧切换到给定帧。框架参数可以是
//	// frame's ID as a string, its WebElement instance as returned by===帧的ID作为字符串，其WebLIST实例由
//	// GetElement, or nil to switch to the current top-level browsing context.===GETEngor，或NIL切换到当前顶级浏览上下文。
//	SwitchFrame(frame interface{}) error
//	// SwitchWindow switches the context to the specified window.===切换窗口将上下文切换到指定的窗口。
//	SwitchWindow(name string) error
//	// CloseWindow closes the specified window.===关闭窗口关闭指定的窗口。
//	CloseWindow(name string) error
//	// ResizeWindow changes the dimensions of a window. If the name is empty, the===ResiZe窗口改变窗口的尺寸。如果名称为空，则
//	// current window will be maximized.===当前窗口将被最大化。
//	ResizeWindow(name string, width, height int) error
//	// FindElement finds exactly one element in the current page's DOM.===Fisher元素在当前页面的DOM中恰好找到一个元素。
//	FindElement(by, value string) (WebElement, error)
//	// FindElement finds potentially many elements in the current page's DOM.===FixEnter在当前页面的DOM中发现了许多元素。
//	FindElements(by, value string) ([]WebElement, error)
//	// ActiveElement returns the currently active element on the page.===Active元素返回页面上的当前活动元素。
//	ActiveElement() (WebElement, error)
//	// DecodeElement decodes a single element response.===解码单元解码单个元素响应。
//	DecodeElement([]byte) (WebElement, error)
//	// DecodeElements decodes a multi-element response.===解码元件对多元素响应进行解码。
//	DecodeElements([]byte) ([]WebElement, error)
//	// GetCookies returns all of the cookies in the browser's jar.===GETCookie返回浏览器jar中的所有cookies。
//	GetCookies() ([]Cookie, error)
//	// GetCookie returns the named cookie in the jar, if present. This method is===如果存在，GETCookie返回jar中的命名Cookie。这种方法是
//	// only implemented for Firefox.===只为Firefox实现。
//	GetCookie(name string) (Cookie, error)
//	// DeleteAllCookies deletes all of the cookies in the browser's jar.===DeleTealCookie删除浏览器jar中的所有Cookie。
//	DeleteAllCookies() error
//	// DeleteCookie deletes a cookie to the browser's jar.===DeleTeCookie删除浏览器的jar的cookie。
//	DeleteCookie(name string) error
//	// Click clicks a mouse button. The button should be one of RightButton,===单击鼠标按钮。按钮应该是右按钮之一，
//	// MiddleButton or LeftButton. ===中间按钮或左按钮。
//	Click(button int) error
//	// DoubleClick clicks the left mouse button twice.===DoubLeCLIK点击鼠标左键两次。
//	DoubleClick() error
//	// ButtonDown causes the left mouse button to be held down.===按钮关闭会导致鼠标左键被按下。
//	ButtonDown() error
//	// ButtonUp causes the left mouse button to be released.===ButoUp导致鼠标左键被释放。
//	ButtonUp() error
//	// SendModifier sends the modifier key to the active element. The modifier===sEd修饰符将修改键发送到活动元素。修饰语
//	// can be one of ShiftKey, ControlKey, AltKey, MetaKey.===可以是ShiftKey，控制中心，AltKey，MetaKey。
//	// Deprecated: Use KeyDown or KeyUp instead.===贬低：使用按键或按键。
//	SendModifier(modifier string, isDown bool) error
//	// KeyDown sends a sequence of keystrokes to the active element. This method===KEYDOWN向活动元素发送键击序列。这种方法
//	// is similar to SendKeys but without the implicit termination. Modifiers are===类似于sEdKEY但没有隐式终止。修饰语是
//	// not released at the end of each call.===在每次调用结束时不释放。
//	KeyDown(keys string) error
//	// KeyUp indicates that a previous keystroke sent by KeyDown should be===KEYUP指示键按下发送的先前击键应该是
//	// released.  释放。
//	KeyUp(keys string) error
//	// Screenshot takes a screenshot of the browser window.===屏幕截图是浏览器窗口的截图。
//	Screenshot() ([]byte, error)
//	// Log fetches the logs. Log types must be previously configured in the===log获取日志。日志类型必须预先配置在
//	// capabilities.  能力。
//	// NOTE: will return an error (not implemented) on IE11 or Edge drivers.===NOTE:将返回IE11或边缘驱动程序上的错误（未实现）。
//	Log(typ log.Type) ([]log.Message, error)
//	// DismissAlert dismisses current alert.===解雇者不理会当前的警戒。
//	DismissAlert() error
//	// AcceptAlert accepts the current alert.===接受者接受当前的警告。
//	AcceptAlert() error
//	// AlertText returns the current alert text.===AlcutTeXT返回当前警告文本。
//	AlertText() (string, error)
//	// SetAlertText sets the current alert text.===StavalTutExt设置当前警告文本。
//	SetAlertText(text string) error
//	// ExecuteScript executes a script. ===Excel脚本执行一个脚本。
//	ExecuteScript(script string, args []interface{}) (interface{}, error)
//	// ExecuteScriptAsync asynchronously executes a script.===ExistUsCurrPaseNyc异步执行脚本。
//	ExecuteScriptAsync(script string, args []interface{}) (interface{}, error)
//	// ExecuteScriptRaw executes a script but does not perform JSON decoding.===ExputsErrPrTrw执行脚本，但不执行JSON解码。
//	ExecuteScriptRaw(script string, args []interface{}) ([]byte, error)
//	// ExecuteScriptAsyncRaw asynchronously executes a script but does not===ExcutsEclipCasyCyRoad异步执行脚本，但不执行
//	// perform JSON decoding.===执行JSON解码。
//	ExecuteScriptAsyncRaw(script string, args []interface{}) ([]byte, error)
//	// WaitWithTimeoutAndInterval waits for the condition to evaluate to true.===WaITWITE TimeOutand Stand等待条件评估为真。
//	WaitWithTimeoutAndInterval(condition Condition, timeout, interval time.Duration) error
//	// WaitWithTimeout works like WaitWithTimeoutAndInterval, but with default polling interval.===WaitWithTimeout像WaitWithTimeoutAndInterval一样工作，但是默认的轮询间隔。
//	WaitWithTimeout(condition Condition, timeout time.Duration) error
//	//Wait works like WaitWithTimeoutAndInterval, but using the default timeout and polling interval.===等待工作类似于WaitWithTimeoutAndInterval，但使用默认超时和轮询间隔。
//	Wait(condition Condition) error
