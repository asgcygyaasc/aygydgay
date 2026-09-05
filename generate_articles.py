from pathlib import Path
import argparse

ROOT = Path(__file__).parent
OUT = ROOT / "articles"
KEYWORDS = ROOT / "keywords.txt"
TG = "TG:qszxc686"

LEADS = [
    "专题盘点", "专题研判", "专题研究", "专题速递", "产业前瞻", "产业剖析", "产业动态", "产业快报", "产业快讯", "产业新风",
    "产业洞察", "产业热点", "产业盘点", "产业观察", "产业解析", "产业走势", "行业聚焦", "行业观察", "行业研读", "行业前瞻",
    "实用指南", "经验参考", "应用观察", "使用手册", "知识整理", "问题梳理", "功能解析", "安全观察", "运营参考", "趋势分析",
]
TOPICS = [
    "微信账号注册方法", "微信账号登录问题", "微信账号安全设置", "微信账号隐私保护", "微信账号绑定管理", "微信账号设备管理", "微信账号异常处理", "微信账号资料维护", "微信账号换机登录", "微信账号迁移准备",
    "微信账号密码管理", "微信账号实名认证说明", "微信账号手机号变更", "微信账号安全中心使用", "微信账号风险提示", "微信账号登录保护", "微信账号好友管理", "微信账号通讯录整理", "微信账号消息管理", "微信账号多设备使用",
    "微信账号新手入门", "微信账号日常维护", "微信账号常见问题", "微信账号操作技巧", "微信账号使用规范", "微信账号隐私设置", "微信账号通知设置", "微信账号权限管理", "微信账号安全检查", "微信账号风险排查",
]
TAILS = [
    "方法与注意事项", "实用技巧整理", "常见问题汇总", "操作思路参考", "安全要点说明", "使用经验分享", "基础知识梳理", "新手入门参考", "详细步骤解析", "重点事项盘点",
    "问题解决思路", "日常维护指南", "设置技巧总结", "注意事项解析", "实操流程说明",
]

PARAGRAPH_PATTERNS = [
    "围绕【关键词】展开说明时，首先需要明确账号的正常使用场景。不同设备、不同网络环境以及不同的安全设置，都会影响实际体验，因此处理问题时应先确认基础信息，再逐项检查相关设置。",
    "对于【关键词】相关问题，很多用户更关心的是操作是否稳定、信息是否安全以及后续维护是否方便。比较稳妥的做法是按照官方功能入口逐步确认，不要为了追求所谓快捷方式而忽略账号安全和个人信息保护。",
    "在日常使用微信账号的过程中，账号资料、绑定信息、登录设备和隐私权限都值得定期检查。尤其在更换手机、修改联系方式或发现异常提示时，应保留必要信息并优先使用平台提供的安全功能。",
    "如果需要处理【关键词】相关事项，可以把问题拆成注册、登录、绑定、安全、隐私和日常维护几个部分。逐项排查通常比反复尝试单一操作更容易定位原因，也能减少误操作造成的额外问题。",
]


def title(i, keyword):
    lead = LEADS[i % len(LEADS)]
    topic = TOPICS[(i // len(LEADS)) % len(TOPICS)]
    tail = TAILS[(i // (len(LEADS) * len(TOPICS))) % len(TAILS)]
    # i is included to guarantee uniqueness while retaining the requested visual style.
    return f"{lead}：{topic}【关键词】{tail}第{i+1}篇"


def article(i, keyword):
    t = title(i, keyword)
    parts = [TG, "", f"# {t}", "", f"## 一、【{keyword}】基础说明", ""]
    seed = (i * 7) % len(PARAGRAPH_PATTERNS)
    for n in range(12):
        p = PARAGRAPH_PATTERNS[(seed + n) % len(PARAGRAPH_PATTERNS)]
        parts += [p.replace("【关键词】", f"【{keyword}】"), ""]
        parts += [f"### 第{n+1}点：实际使用中的关注事项", ""]
        parts += [f"第{n+1}点主要围绕【{keyword}】展开。实际操作时，应先确认账号属于本人正常使用范围，再检查登录环境、绑定信息和安全提醒。对于陌生链接、非官方页面以及要求提供验证码的请求，应保持谨慎，避免泄露账号信息。", ""]
    parts += ["## 二、日常维护建议", "", f"完成【{keyword}】相关设置后，建议定期检查登录设备、隐私权限和绑定资料。遇到异常登录、频繁验证或无法正常使用等情况，应优先查看微信客户端提供的提示，并按照官方流程处理。", ""]
    parts += ["## 三、总结", "", f"总体来看，【{keyword}】的重点不是追求复杂操作，而是建立清晰、稳定和安全的使用习惯。无论是新用户还是长期使用者，都可以从账号资料、登录安全、隐私保护和设备管理几个方向进行检查。", ""]
    return "\n".join(parts)


def load_keywords():
    values = [x.strip() for x in KEYWORDS.read_text(encoding="utf-8").splitlines() if x.strip()]
    if not values:
        raise SystemExit("keywords.txt 不能为空")
    return values


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--replace-only", action="store_true")
    args = ap.parse_args()
    kws = load_keywords()
    OUT.mkdir(exist_ok=True)
    if args.replace_only:
        # Rebuild files from the current keyword list; filenames remain stable.
        pass
    for i in range(900):
        kw = kws[i % len(kws)]
        path = OUT / f"{i+1:04d}.md"
        path.write_text(article(i, kw), encoding="utf-8")
    print(f"generated 900 articles using {len(kws)} keywords in a round-robin cycle")

if __name__ == "__main__":
    main()
