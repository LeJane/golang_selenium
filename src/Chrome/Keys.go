package Chrome

//QQ:29295842  希望大家多多来交流
//import (
//	"fmt"
//	//	"log"

//	"github.com/tebeka/selenium"
//	"github.com/tebeka/selenium/chrome"
//	//	"os/exec"
//	//	"strings"
//	//	"g"
//	//"reflect"
//	//	"errors"
//	//"strconv"
//	"strings"
//	//	"github.com/axgle/mahonia"
//)
//按键
//===================================================================
func Chrome_Keys_data(name string) string {
	if name == "NULL" {
		return NULL
	}
	if name == "CANCEL" {
		return CANCEL //^break
	}
	if name == "HELP" {
		return HELP
	}
	if name == "BACKSPACE" || name == "BACK_SPACE" { //删除键
		return BACKSPACE
	}
	if name == "TAB" {
		return TAB //TAB键
	}
	if name == "CLEAR" {
		return CLEAR
	}
	if name == "RETURN" {
		return RETURN
	}
	if name == "ENTER" {
		return ENTER //回车键
	}
	if name == "SHIFT" || name == "LEFT_SHIFT" {
		return SHIFT //Shift键
	}
	if name == "CONTROL" || name == "LEFT_CONTROL" { //Ctrl 键
		return CONTROL
	}
	if name == "ALT" || name == "LEFT_ALT" {
		return ALT //Alt 键
	}
	if name == "PAUSE" {
		return PAUSE
	}
	if name == "ESCAPE" {
		return ESCAPE //ECS键
	}
	if name == "SPACE" {
		return SPACE //空格键
	}
	if name == "PAGE_UP" {
		return PAGE_UP //PgUp 键
	}
	if name == "PAGE_DOWN" {
		return PAGE_DOWN //PgDwon 键
	}
	if name == "END" {
		return END //END 键
	}
	if name == "HOME" {
		return HOME //HOME 键
	}
	if name == "LEFT" || name == "ARROW_LEFT" {
		return LEFT //左键
	}
	if name == "UP" || name == "ARROW_UP" {
		return UP //上键
	}
	if name == "RIGHT" || name == "ARROW_RIGHT" { //右键
		return RIGHT
	}
	if name == "DOWN" || name == "ARROW_DOWN" {
		return DOWN //下键
	}
	if name == "INSERT" {
		return INSERT //insert键
	}
	if name == "DELETE" {
		return DELETE //del键
	}

	//	if name == "" {
	//		return SEMICOLON //';'键
	//	}
	//	if name == "" {
	//		return EQUALS //'='键
	//	}
	//数字键盘
	if name == "NUMPAD0" {
		return NUMPAD0 // number pad keys
	}
	if name == "NUMPAD1" {
		return NUMPAD1
	}
	if name == "NUMPAD2" {
		return NUMPAD2
	}
	if name == "NUMPAD3" {
		return NUMPAD3
	}
	if name == "NUMPAD4" {
		return NUMPAD4
	}
	if name == "NUMPAD5" {
		return NUMPAD5
	}
	if name == "NUMPAD6" {
		return NUMPAD6
	}
	if name == "NUMPAD7" {
		return NUMPAD7
	}
	if name == "NUMPAD8" {
		return NUMPAD8
	}
	if name == "NUMPAD9" {
		return NUMPAD9
	}
	if name == "MULTIPLY" {
		return MULTIPLY // '*' 键
	}
	if name == "ADD" {
		return ADD // '+' 键
	}
	if name == "SEPARATOR" {
		return SEPARATOR //','键
	}
	if name == "SUBTRACT" {
		return SUBTRACT // '-' 键
	}
	if name == "DECIMAL" {
		return DECIMAL // '.'键
	}
	if name == "DIVIDE" {
		return DIVIDE //'/'键
	}

	if name == "F1" {
		return F1 // function  keys
	}
	if name == "F2" {
		return F2
	}
	if name == "F3" {
		return F3
	}
	if name == "F4" {
		return F4
	}
	if name == "F5" {
		return F5
	}
	if name == "F6" {
		return F6
	}
	if name == "F7" {
		return F7
	}
	if name == "F8" {
		return F8
	}
	if name == "F9" {
		return F9
	}
	if name == "F10" {
		return F10
	}
	if name == "F11" {
		return F11
	}
	if name == "F12" {
		return F12
	}

	if name == "META" {
		return META
	}
	if name == "COMMAND" {
		return COMMAND
	}
	//return name
	return ""
}

//===================================================================
