from pathlib import Path
import re

ROOT = Path(__file__).parent
OUT = ROOT
KEYWORDS = ROOT / "keywords.txt"
TG = "TG:qszxc686"
LEADS = ["专题盘点", "专题研判", "专题研究", "专题速递", "产业前瞻", "产业剖析", "产业动态", "产业快报", "产业快讯", "产业新风", "产业洞察", "产业热点", "产业盘点", "产业观察", "产业解析", "产业走势", "行业聚焦", "行业观察", "行业研读", "行业前瞻", "实用指南", "经验参考", "应用观察", "使用手册", "知识整理", "问题梳理", "功能解析", "安全观察", "运营参考", "趋势分析"]
TOPICS = ["微信账号注册方法", "微信账号登录问题", "微信账号安全设置", "微信账号隐私保护", "微信账号绑定管理", "微信账号设备管理", "微信账号异常处理", "微信账号资料维护", "微信账号换机登录", "微信账号迁移准备", "微信账号密码管理", "微信账号实名认证说明", "微信账号手机号变更", "微信账号安全中心使用", "微信账号风险提示", "微信账号登录保护", "微信账号好友管理", "微信账号通讯录整理", "微信账号消息管理", "微信账号多设备使用", "微信账号新手入门", "微信账号日常维护", "微信账号常见问题", "微信账号操作技巧", "微信账号使用规范", "微信账号隐私设置", "微信账号通知设置", "微信账号权限管理", "微信账号安全检查", "微信账号风险排查"]
TAILS = ["方法与注意事项", "实用技巧整理", "常见问题汇总", "操作思路参考", "安全要点说明", "使用经验分享", "基础知识梳理", "新手入门参考", "详细步骤解析", "重点事项盘点", "问题解决思路", "日常维护指南", "设置技巧总结", "注意事项解析", "实操流程说明"]
OPENERS = [
"围绕【关键词】展开说明时，首先需要明确账号的正常使用场景。不同设备、不同网络环境以及不同的安全设置，都会影响实际体验，因此处理问题时应先确认基础信息，再逐项检查相关设置。",
"对于【关键词】相关问题，很多用户更关心的是操作是否稳定、信息是否安全以及后续维护是否方便。比较稳妥的做法是按照官方功能入口逐步确认，不要为了追求快捷方式而忽略账号安全和个人信息保护。",
"在日常使用微信账号的过程中，账号资料、绑定信息、登录设备和隐私权限都值得定期检查。尤其在更换手机、修改联系方式或发现异常提示时，应保留必要信息并优先使用平台提供的安全功能。",
"如果需要处理【关键词】相关事项，可以把问题拆成注册、登录、绑定、安全、隐私和日常维护几个部分。逐项排查通常比反复尝试单一操作更容易定位原因，也能减少误操作造成的额外问题。",
]
POINTS = ["先看账号基础资料", "再检查登录环境", "确认绑定信息", "核对隐私权限", "查看安全提醒", "整理常用设备", "处理异常提示", "做好日常维护"]

def make_title(i, keyword):
    return f"【{keyword}】{LEADS[i % len(LEADS)]}：{TOPICS[(i // len(LEADS)) % len(TOPICS)]}{TAILS[(i // (len(LEADS) * len(TOPICS))) % len(TAILS)]}第{i+1}篇"

def safe_filename(title):
    name = re.sub(r'[\\/:*?"<>|]', '-', title).strip().strip('.')
    return f"{name}.md"

def para(i, n, keyword):
    base = OPENERS[(i + n * 3) % len(OPENERS)].replace("【关键词】", f"【{keyword}】")
    extra = f"在第{n+1}个检查环节中，还可以结合自己的使用习惯进行确认。不要把一次成功操作理解为永久有效，设备变化、系统升级和安全策略调整都可能让原来的设置发生变化。"
    return base + extra

def make_article(i, keyword):
    title = make_title(i, keyword)
    layout = i % 6
    parts = [TG, "", f"# {title}", ""]
    if layout == 0:
        parts += [f"## 一、【{keyword}】基础认识", ""]
        for n in range(8): parts += [f"### {n+1}、{POINTS[(i+n)%len(POINTS)]}", "", para(i,n,keyword), ""]
        parts += ["## 二、使用过程中的常见情况", "", para(i,8,keyword), "", para(i,9,keyword), "", "## 三、总结", "", para(i,10,keyword)]
    elif layout == 1:
        parts += [f"## 一、先明确【{keyword}】的使用目标", "", para(i,0,keyword), "", "## 二、分步骤检查", ""]
        for n in range(7): parts += [f"**步骤{n+1}｜{POINTS[(i+n*2)%len(POINTS)]}**", "", para(i,n+1,keyword), ""]
        parts += ["## 三、容易忽略的细节", "", para(i,9,keyword), "", "## 四、结语", "", para(i,10,keyword)]
    elif layout == 2:
        parts += [f"## 一、问题背景", "", para(i,0,keyword), "", f"## 二、【{keyword}】重点观察表", "", "| 项目 | 关注内容 | 建议 |", "| --- | --- | --- |"]
        for n in range(8): parts += [f"| {POINTS[(i+n)%len(POINTS)]} | 账号使用与安全 | 按官方功能逐项确认 |"]
        parts += ["", "## 三、补充说明", "", para(i,9,keyword), "", para(i,10,keyword), "", "## 四、总结", "", para(i,11,keyword)]
    elif layout == 3:
        parts += [f"## 一、【{keyword}】快速梳理", "", para(i,0,keyword), "", "## 二、为什么需要定期检查", "", para(i,1,keyword), ""]
        for n in range(2,10): parts += [f"### 重点 {n-1}", "", para(i,n,keyword), ""]
        parts += ["## 三、实际使用建议", "", para(i,10,keyword), "", para(i,11,keyword)]
    elif layout == 4:
        parts += [f"> 本文围绕【{keyword}】整理基础使用与安全注意事项。", "", f"## 一、核心结论", "", para(i,0,keyword), "", "## 二、详细展开", ""]
        for n in range(1,9): parts += [f"### {POINTS[(i+n*3)%len(POINTS)]}", "", para(i,n,keyword), ""]
        parts += ["## 三、风险与边界", "", "不要向任何非官方页面提供密码、短信验证码或其他敏感验证信息。遇到异常情况，应以客户端和官方帮助渠道的提示为准。", "", "## 四、结论", "", para(i,10,keyword)]
    else:
        parts += [f"## 【{keyword}】内容导读", "", para(i,0,keyword), "", "### 01 基础准备", "", para(i,1,keyword), "", "### 02 操作检查", "", para(i,2,keyword), "", "### 03 安全设置", "", para(i,3,keyword), "", "### 04 隐私管理", "", para(i,4,keyword), "", "### 05 设备变化", "", para(i,5,keyword), "", "### 06 异常处理", "", para(i,6,keyword), "", "### 07 后续维护", "", para(i,7,keyword), "", "## 最后说明", "", para(i,10,keyword)]
    return "\n".join(parts) + "\n"

def load_keywords():
    values = [x.strip() for x in KEYWORDS.read_text(encoding="utf-8").splitlines() if x.strip()]
    if not values: raise SystemExit("keywords.txt 不能为空")
    return values

def main():
    kws = load_keywords()
    for i in range(900):
        keyword = kws[i % len(kws)]
        title = make_title(i, keyword)
        (OUT / safe_filename(title)).write_text(make_article(i, keyword), encoding="utf-8")
    print(f"generated 900 articles with front-loaded keywords using {len(kws)} keywords")

if __name__ == "__main__": main()
