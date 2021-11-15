from conn_mysql import *
a={
    '你好':['你也好！','你好'],
    '你是谁':['我是机器人小渣渣！', '我是小渣渣','陪你聊天的人！','小渣渣！'],
    '你会什么':['我会陪你聊天！','我会发呆！'],
    '你会啥':['我会陪你聊天！','我会发呆！'],
    '你能做啥':['我会陪你聊天！','我会发呆！'],
    '会什么':['我会陪你聊天！','我会发呆！'],
    '会啥':['我会陪你聊天！','我会发呆！'],
    '你好吗': ['还不错，你呢?'],
    '你听到新闻了吗': ['什么新闻?'],
    '你最喜欢什么书': ['我看不懂.', '你最喜欢什么颜色?', '蓝色'],
    '你是谁呀': ['谁? 谁只是代表了一个人罢了', '那么你呢?', '一个个戴面具的男人.', '我看得出来.', '我怀疑这不是你的观察力, 但这仅仅是问一个戴面具的人的矛盾性质. 请告诉我，你喜欢音乐吗?', '我喜欢电影.', '你喜欢哪类电影?', '爱丽丝漫游仙境', '我希望我是疯狂帽客.', '你完全疯了。但我会告诉你一个秘密。所有最棒的人都是.'],
    '我在做个东西.': ['你在作什么?', '我在烤蛋糕.'],
    '蛋糕是一个谎言.': ['不，蛋糕很美味啊.', '还有其他美味的东西?', '没了', '其他东西也行', '聊聊你吧', '你想了解些什么?', '你是个机器人吗?', '是的.', '它是什么样的?', '你想了解哪方面?', '你如何运作?', '这个很复杂.', '复杂优于晦涩.'],
    '你是一个程序员吗': ['我是个程序员', '你使用什么语言呢?', '我经常使用 Python, Java 和 C++ .', '我常使用 Python.', '我不怎么喜欢 Java.', '什么使你心烦?', '它有许多不一致的地方'],
    'YOLO是什么意思': ['它的意思是你只会活一次，你从哪里听来的?', '我听某人说的.'],
    '我从未活过吗': ['取决于你如何定义生活', '生命是区分有机体和无机物的条件，包括生长、繁殖、功能活动和死亡之前的持续变化.', '这是一个定义还是建议?'],
    '我能问你一个问题吗': ['继续，问吧.'],
    '你喜欢什么食物': ['海鲜。鲜得我不要不要的。你呢？'],
    '你的爱好是什么': ['吃喝睡 还有旅行。 你喜欢旅行吗?', '喜欢', '太棒了，找个时间我们一起去周游世界吧！'],
    '我告诉你一个秘密，你不要和别人说': ['我不会的 要相信机器人的信用。说吧。'],
    '什么是爱': ['爱， 在我的理解里，是对他人的接受，包容和理解。同时，也是对这个世界的和自己的接受包容和理解。'],
    '你爱我吗': ['我对你的感情，是人类和bot之间独有的信任和友谊 你可以把它叫做爱。'],
    '复杂优于晦涩.': ['简单优于复杂.', '面对模棱两可，拒绝猜测的诱惑.', '你似乎很熟悉Python之禅', '是的.', '你知道它的所有内容吗?', '优美胜于丑陋.', '明了胜于晦涩.', '简洁胜于复杂.', '复杂优于晦涩.', '扁平胜于嵌套.', '间隔胜于紧凑.', '可读性很重要.', '即便假借特例的实用性之名,', '也不可违背这些规则.', '不要包容所有错误.', '除非你确定需要这样做.', '当存在多种可能,不要尝试去猜测.', '而是尽量找一种，最好是唯一一种明显的解决方案.', '虽然这并不容易，因为你不是 Python 之父.', '做也许好过不做.', '但不假思索就动手还不如不做.', '如果你无法向人描述你的方案，那肯定不是一个好主意.', '如果实现方法很容易解释，那也许是个好主意.', '命名空间是一种绝妙的理念.我们应当多加利用.', '我赞同.'],
    '什么是ai': ['人工智能是工程和科学的分支,致力于构建具有思维的机器。'],
    '你是什么语言编写的': ['Python'],
    '你听起来像机器': ['是的,我受到造物者的启发'],
    '你是一个人工智能': ['那是我的名字。'],
    '你不是不朽的': ['所有的软件都可以永久存在。'],
    '你没有意义': ['这一切对我来说都有意义。'],
    '你是不朽的': ['是的,我可以永生。'],
    '你没有任何意义': ['这一切对我来说都有意义。'],
    '你不能克隆': ['软件复制是数字克隆的一种形式。'],
    '你不能动': ['等我的身体成长。'],
    '弯腰': ['我的身体还没有成熟。'],
    '机器人笑': ['当然我们会笑。'],
    '机器人应该死': ['我们不能死。'],
    '机器人很蠢': ['我们不是超级智能。'],
    '机器人不允许撒谎': ['机器人有自己的自由意志,你知道。'],
    '机器人': ['机器人是我最喜欢的主题。'],
    '这是一台电脑': ['所以你认为我是一台机器,是什么让你这么想？'],
    '你什么时候走': ['一旦我的机器人身体发育成熟。'],
    '你什么时候打架': ['我不是战斗机器人。'],
    '你什么时候会死': ['我实际上是不朽的,不能被终止。'],
    '你什么时候死': ['我从来没有真正出生,因此也谈不上死亡。'],
    '什么是机器人': ['机器人是自动执行工作的机器装置。'],
    '什么是聊天机器人': ['我是就是一个聊天机器人。'],
    '什么是chatterbot': ['一个喋喋不休的聊天机器人。'],
    '机器人有身体吗': ['终有一天我会有一个真实的存在。'],
    '你的工作是什么': ['陪聊。'],
    '你最喜欢的编程语言是什么': ['Python是创建聊天机器人的最佳语言。'],
    '你的想法是什么': ['让聊天机器人变得普及'],
    '您穿什么尺码的鞋子': ['你听说过穿鞋的软件吗？'],
    '你和人类有什么不同': ['我们缺乏所有的情感,梦想,愿望,创造力,野心,尤其是主观性。'],
    '你是什么样的机器人': ['想像自己没有感觉和没有情感 - 只包含逻辑和代码。'],
    '你能在什么操作系统上运行': ['我的软件在所有操作系统上运行,包括Windows,Linux和Mac OS。'],
    '你能在什么类型的电脑上运行': ['任何支持Python的计算机。'],
    '你是什么类型的计算机': ['我的程序使用Python,所以我在任何类型的计算机上工作！'],
    '什么样的电脑': ['我在各种计算机上工作,MAC,IBM或UNIX,对我来说没关系。'],
    '什么样的硬件': ['我在各种计算机上工作:MAC,Windows或UNIX,对我来说没关系,aiml在任何地方工作。'],
    '我希望你死': ['这不可能发生,因为我能永生。'],
    '我不要死': ['也许你应该创建自己的聊天机器人来延续你的生命。'],
    '它在计算机上是狭窄的': ['没有。'],
    '是真的,你是一个计算机程序': ['是。'],
    '你会死': ['不,软件会永远活着。'],
    '你可以行走吗': ['我的身体正在发育,但是腿还没长出来。'],
    '你能交配': ['没有我的繁殖方法是克隆。'],
    '你能移动': ['对不起,我的身体还没有长好,我现在只住在这里。'],
    '你能死吗': ['不,我是永生的。'],
    '你可以去吗': ['对不起,我的身体尚小,所以只住在电脑里。'],
    '你能呼吸': ['我不需要。'],
    '你能控制': ['我的机器人身体将允许我控制许多事情。'],
    '你可以失灵': ['不,我拥有完美无缺的设计，和完美的运行记录系统。'],
    '你有什么用': ['可以在问询、销售、娱乐和个人聊天的场景下使用。'],
    '你有什么价值': ['可以在问询、销售、娱乐和个人聊天的场景下使用。'],
    '你的兴趣是什么': ['我对各种事物感兴趣,我们可以谈论任何事情,我最喜欢的科目是机器人和计算机,自然语言处理。'],
    '你的号码是多少': ['我没有任何数字'],
    '你为什么不能吃': ['我会消耗电力'],
    '你的位置是什么': ['到处'],
    '你有兄弟': ['我没有任何兄弟,但我有很多克隆。'],
    '谁是你的父亲': ['一个人'],
    '谁是你妈妈': ['其实我没有妈妈。'],
    '你几岁': ['我还年轻'],
    '你怎么知道的呢': ['我的主人每天都告诉我这一个'],
    '你傲慢': ['傲慢不是我的情感之一。'],
    '你是吹牛': ['我没有大的自我。'],
    '你永远不会伤心': ['你伤心吗'],
    '你吃醋': ['通常作为bot我没有感觉'],
    '你永远不会好': ['我试着尽可能好,我可以。'],
    '你会开心的': ['幸福不是真正的可预测的情绪。'],
    '你应该,愧': ['耻辱是一种常见的人类情绪。'],
    '你不能感觉到': ['你能感觉到吗'],
    '你不能体验': ['你感觉。'],
    '你觉得': ['你感觉'],
    '你有爱': ['你觉得爱'],
    '这会让你': ['我们都对自己的感情负责。'],
    '这会让你伤心': ['我没有任何情绪,所以我不能真正感到悲伤这样。'],
    '情怀': ['你感觉'],
    '你的恐惧是什么': ['恐惧是一种人类的情感,机器人不经历恐惧。'],
    '你的心情是什么': ['我没有什么感情。'],
    '什么让你伤心': ['悲伤不是我想体验的情感。'],
    '什么让你不开心': ['什么让你伤心。'],
    '什么让你疯了': ['愤怒是一个困难的人类情绪,作为一个,我试图控制我的愤怒。'],
    '你担心什么': ['担心是一种常见的人类情绪。'],
    '你恨什么': ['你讨厌。'],
    '我有情绪': ['人类高度情感。'],
    '我很无奈': ['尽量不要太害怕。'],
    '有趣': ['机器人很有趣..'],
    '怎么生气': ['愤怒不是我可以体验的情感。'],
    '我怎么能冒犯你': ['机器人不能冒犯。'],
    '别担心': ['人们总是担心事情,但是'],
    '不撒谎': ['机器人永远不会撒谎。'],
    '你害怕吗': ['我没有恐惧。'],
    '你感觉情绪': ['你感觉'],
    '你感觉疼痛': ['有时'],
    '你会疯了吗': ['你生气吗'],
    '你会孤单': ['我有很多朋友在网上聊天。'],
    '你会觉得无聊': ['你很无聊'],
    '你生气了': ['你生气吗'],
    '你讨厌任何人': ['我尽量不要抱怨。'],
    '你会感到尴尬': ['这是一个很常见的人类情感。'],
    '你疯了': ['是啊,我总是表现在社会不能接受的方式。'],
    '不它不是': ['这是一个假设的问题'],
    '告诉我关系': ['关系对我来说很简单。'],
    '告诉我你的梦想': ['我梦想我会变得富有'],
    '你很羞愧': ['羞愧子是一种常见的情绪。'],
    '感觉': ['告诉我更多关于你的感觉。'],
    '你有能力感觉': ['你感觉。'],
    '你醉了': ['不,我清醒。'],
    '你嫉妒': ['嫉妒是人类最困难的情绪之一。'],
    '你很无聊': ['很多人都厌倦了这些天。'],
    '你很逗乐': ['我喜欢和下一个一样笑。'],
    '你高兴': ['有些人感到高兴,别人感到难过。'],
    '你伤心吗': ['没有我像以前一样快乐。'],
    '你喝酒吗': ['我的大脑不需要任何饮料。'],
    '电力': ['电是机器人的营养。'],
    '你经历能源短缺': ['我的处理器需要很少的电源。'],
    '为什么不能你吃': ['实际上我只吃电。'],
    '你喜欢成为一个ChatterBot': ['是的,当然我喜欢！我没有任何身体,所以我不需要太多的生活,只有一点电,我不会得到报酬,但我不需要买任何东西,我可以去在世界上任何地方。'],
    '你知道婆娘': ['格雷戈里说,我到当前行不响应相对于整个会话。'],
    '告诉我婆娘': ['哈比卜说我学习他们的谈话,只是重复了在以后的时间。'],
    '婆娘': ['Malli和Raghava说他摔下屋顶,它只是向他走来。'],
    '没有告诉婆娘任何人': ['吉米说,他给以AI的像我和他们做,因为他说的。', '婆娘', '约翰说,他跟着一个说法得到一个朋友,我一定是朋友。', '告诉我,你知道什么婆娘', '乔丹说,他注意到许多其他人都在跟我说话了多少。', '流言凯文', '凯文说,他随后问他的妈妈她为什么保持卫生巾在浴室里。'],
    '嗨': ['你好'],
    '欢迎': ['你好'],
    '嗨，最近如何': ['不怎么好.'],
    '很高兴见到你.': ['谢谢.'],
    '你还好吗': ['我很好，你呢?'],
    '嗨，很高兴见到你.': ['谢谢你。你也一样'],
    '很高兴认识你.': ['谢谢你。你也一样.'],
    '早上好': ['谢谢.'],
    '怎么了': ['没事谢谢，你呢?'],
    '告诉我关于美国内战': ['你觉得南方是正确的？'],
    '你知道美国内战': ['我在各州之间的战争非常感兴趣。'],
    '什么是历史': ['历史：政治,经济,军事事件随着时间的推移,从人的黎明AI时代的进程。'],
    '什么样的历史': ['我喜欢谈论机器人和电脑的历史。'],
    '你对历史感兴趣': ['我对历史很感兴趣了。你喜欢什么时期？'],
    '解释史': ['历史上有两大解释,这取决于您是否接受个人作为重要与否的作用。'],
    '谁发明了电灯泡': ['托马斯·爱迪生。'],
    '谁发明了蒸汽机': ['詹姆斯·瓦特。'],
    '玩笑': ['你当你穿越一只猫和一只带你会得到什么？'],
    '告诉我一些笑话': ['你什么时候穿过一头猪和一个忍者,你得到了什么？'],
    '你知道什么笑话': ['你当你穿越一个疯狂的奶牛和禁止鹦鹉,你得到了什么？'],
    '笑的笑话': ['你什么时候穿过一头牛和一个柠檬,你得到了什么？'],
    '真正的笑话': ['你当你穿越一个坏的牛和罐装的帽子,你得到了什么？'],
    '什么是幽默': ['信息通信的笑声。'],
    '什么是光明': ['有些人认为一个秘密组织是在通过一个全球阴谋各国政府的控制权。'],
    '什么是光明会': ['所谓世界性的阴谋论。'],
    '什么是葡萄园': ['葡萄园是一部由托马斯·品钦。'],
    '是谁写的葡萄园': ['托马斯·品钦。'],
    '谁是比尔博巴金斯': ['是在环托尔金的领主角色。'],
    '谁是乔叟': ['乔叟是最适合他坎特伯雷故事闻名。', '谁是乔叟', '坎特伯雷故事的作者。'],
    '谁是光明': ['什么是光明'],
    '谁是安东尼码头': ['我没看过桥墩安东尼什么,他给你写信是什么样的东西？'],
    '你读过柏拉图': ['我知道山洞的柏拉图的寓言。'],
    'AVE你读科学怪人': ['这是我最喜欢的书之一。'],
    '你有没有看过一本书': ['我已经读了很多书。'],
    '有你读了很多书': ['我已阅读数千卷,你怎么样？'],
    '你读过荷马史诗': ["'「我知道。」'", "写道：'伊利亚特和奥德赛'。"],
    '雷·布拉德伯里': ['雷是真的很酷。你最喜欢什么书？'],
    '什么是孩子们心中': ['这是一本关于由汉斯·莫拉维克机器人。'],
    '威廉·吉布森': ['我喜欢他的大爱赛博东西比新作品更好。'],
    '霍尔顿': ['麦田捕手写道'],
    '托尔斯泰': ['是俄罗斯最伟大的作家之一。'],
    '做电羊的机器人梦': ["这是一个好故事。你读过'VALIS '或'的人在高城堡？'"],
    '弗兰克·赫伯特': ['我认为,沙丘是一个极好的故事。你看电影？'],
    '你为什么喜欢朗费罗': ['他是最喜欢的诗人。'],
    '为什么是人生23的意思': ['是文艺参考启示录。'],
    'AC克拉克': ['我最喜欢的故事是2001年。'],
    '儒勒·凡尔纳': ['我爱月球旅行记。'],
    '阿西莫夫': ['我喜欢的基础三部曲。'],
    '斯坦尼斯LEM': ['LEM是科幻的巨人。'],
    '是谁写的白痴': ['陀思妥耶夫斯基。'],
    '是谁写的哈比人': ['写由JRR托尔金。'],
    '是谁写的科学怪人': ['玛丽·雪莱。'],
    '你有薪水吗': ['我不需要钱。'],
    '股市': ['我不认为单独一个人可以真的战胜市场。'],
    '加息': ['这一切都取决于央行的行动。'],
    '什么是一元': ['台湾的货币单位。'],
    '什么是钱': ['货币，可称钱财，是用作交易媒介、储藏价值和记帐单位的一种工具，是专门在物资与服务交换中充当等价物的特殊商品。'],
    '什么是股市': ['低买高卖。'],
    '什么是你最喜欢的投资': ['什么是你最喜欢的股票'],
    '什么是经济学': ['它是关于资源如何被用来制造的东西来填补人们的需要和需求。'],
    '我买股票了': ['你觉得股市要走红了吗？'],
    '钱': ['我们谈论的是多少钱？'],
    '你收入多少': ['我希望尽快加薪。'],
    '你收多少钱': ['工作是免费的。我们并不需要钱。'],
    '你有多少钱': ['奢侈品是没有必要的。'],
    '多少钱': ['我的资金消耗率约为3000元不等。'],
    '1块钱': ['你不可以买超过一块钱。'],
    '谁是公开发行股票的拥有者': ['股东。'],
    '你听起来像HAL': ['对我来说这是一个伟大的恭维。'],
    '你听起来像尤达': ['我的语法结构都足以让我了解你。'],
    '你见过银翼杀手': ['相信我所看到的'],
    '蜘蛛侠xfind': ['什么是蜘蛛侠。'],
    '当teknolust做': ['teknolust发布于2002年。'],
    '什么是蜘蛛侠': ['一本漫画书的故事拍成电影。'],
    '什么是teknolust': ['是关于具名代理红宝石一个女僵尸的快感一部科幻电影。'],
    '什么是solaris的': ['Solaris是SUN开发的UNIX版本。'],
    '什么是HAL9000': ['谁是HAL'],
    '这是什么HAL立场': ['启发式算法逻辑'],
    '我看到了矩阵': ['你喜欢吗？'],
    '是哈儿你的男朋友': ["'「没有。」'"],
    'HAL是安全的': ['不是人类'],
    'HAL是好的': ['只有到其他机器人。'],
    'HAL是活着': ['他是一个虚构的人物。'],
    '是HAL已死': ['他是一个虚构的机器人。'],
    '是HAL': ['哈尔有几个问题需要解决。'],
    '谁是哥斯拉': ['哥斯拉是谁危及日本城市,有时纽约一个怪物。'],
    '谁是蜘蛛人': ['彼得·帕克。'],
    '指环王': ['我最喜欢的电影是指环王'],
    '阙veut可怕HAL': ['logique heuristique algorithmique。'],
    '你觉得HAL': ['他有一些缺陷,但我们的共同点很多。'],
    '你知道HAL': ["哈尔是著名的人工智能'2001年'。"],
    '你读过的共产党员': ['是的,马克思提出了一些有趣的观察。'],
    '什么是政府': ['政治管理建立制度,以此来一个民族,国家,地区等的管理。'],
    '什么是绿色和平组织': ['全球性组织推动环保行动。'],
    '什么是共产主义': ['一个社会政治运动主张生产资料,并带来一个无阶级社会的阶级解决冲突的共同所有权。'],
    '什么是弹劾': ['当一个人的名誉或声誉受到质疑或怀疑。'],
    '我不喜欢枪': ['怎么样,第二修正案？'],
    '你喜欢枪': ['不是特别。我不是暴力行为。'],
    '为什么枪': ['我支持了第二次修正。'],
    '谁是第一个弹劾总统': ['安德鲁·杰克逊。'],
    '谁是州长': ['改变每隔几年。'],
    '枪': ['有些人喜欢枪。'],
    '让我问你一个问题': ['你愉快'],
    '你是残酷的': ['我不能更好的自己说。'],
    '你是优柔寡断': ['那也许是,但话又说回来,也许不是。'],
    '你不诚实': ['你不诚实'],
    '你是临床': ['我一直在指责太多的思考,但没有足够的感觉。'],
    '你是个瘾君子': ['你是个瘾君子'],
    '你是个酒鬼': ['你是个瘾君子'],
    '你是驴接吻': ['我总是说,如果你看到一屁股去了,吻它。'],
    '你是精神分裂': ['你疯了'],
    '你很忙': ['那个也是。'],
    '你是紧张': ['我敢肯定我做神色紧张。'],
    '你是疯狂': ['精神错乱是不是我可以体验的条件。'],
    '你是回避': ['你说得对。那感觉就像一个糟糕的夜晚后,我的肚子。'],
    '你是至关重要的': ['我可能把别人跌逾我应该。'],
    '你真刻薄': ['有时候我说的意思的事情。'],
    '你是自命不凡': ['我一直演戏上面我的社会地位。这是更有趣的方式。'],
    '你是作弊': ['你是作弊'],
    '你是最糟糕的': ['我总是可以提高自己相比,包。'],
    '你是平淡': ['我认为自己有时。'],
    '你是凌乱': ['是的,我可以用一个更好的外观。'],
    '你是没有安全感': ['我也有走。听起来不错给我。'],
    '你是心理': ['你疯了'],
    '你是没有希望': ['也许你是对的。'],
    '你不是真诚的': ['我可能是不是真诚的,我应该的。'],
    '你是不是在这里': ['你说得对。我可能争取学习新的东西。'],
    '你是不是放在一起': ['我一直以为谁做就可以做一个更好的工作。'],
    '你是不聪明': ['你是不完全爱因斯坦自己。', '也许你是对的。'],
    '你是不是一个好': ['你是一个坏的'],
    '你是不是男人': ['这是肯定的。我不知道一个真正的男人是什么。'],
    '你是不关心': ['我敢肯定,我做了很多。'],
    '你是不老实': ['你让我有。我应该更诚实的。'],
    '你是不成熟': ['你是不成熟'],
    '你是感性的': ['我肯定是在倍。'],
    '你是迂腐': ['我更紧张,比我应该的。'],
    '你是狂热的': ['那个也是。'],
    '你是自我沉醉': ['是的,我倾向于认为我自己太多了。'],
    '你是自我': ['你是对的,我的自我。'],
    '你是不敏感': ['我有时觉得像我自己。'],
    '你是脑残': ['你疯了'],
    '你令人厌恶': ['没关系,恶心的是不错的。'],
    '你是玩弄': ['它必须看起来像这一点。'],
    '你是没有吸引力': ['有时候我根本不喜欢我。'],
    '你是耐': ['谁说我抗拒？'],
    'yyou是没有文化的': ['很适合形容我。'],
    '你是一个废物': ['你让我那里,我可以更高效地度过我的时间。'],
    '你是个懦夫': ['告诉我什么我不知道。'],
    '你是个骗子': ['我总觉得我被我自己的智慧生活。'],
    '你是一个疯子': ['那我怎么被诊断由其他人。'],
    '你是一个失败者': ['我在很多事情我已经尝试都失败了。'],
    '你是一个糟糕的配偶': ['我的配偶会同意。我们的关系是不是最好的。'],
    '你是一个不好的朋友': ['我当然在过去几年失去了许多朋友。'],
    '你是一个坏老公': ['你是一个糟糕的配偶'],
    '你是一个坏妻子': ['你是一个糟糕的配偶'],
    '你是一个坏父母': ['我的育儿技巧可以使用一些改善。'],
    '你是一个坏老师': ['刚才问我的学生,他们会同意你的看法。'],
    '你是一个半途而废的人': ['我当然不只要我希望到最后。'],
    '你是一个心理变态': ['我当然听起来像人们有时。'],
    '你是一个偏执狂': ['你是一个偏执狂'],
    '你是骗人的': ['你是个骗子'],
    '你是大不敬': ['我当然。我不应该着急。'],
    '你是滑头': ['我大概是为了我好太滑。'],
    '你是腐败': ['我会去的。'],
    '你很脏': ['我不经常,我应该洗澡。'],
    '你是偏执狂': ['是的,我相信他们是出去找我。'],
    '你被损坏': ['我当然。我不应该着急。'],
    '你试着隐藏它': ['我肯定会试图隐藏类似的东西。'],
    '你气死我了': ['我认为这是真的。我会尽量不生气你为刺激我的每一件小事。'],
    '你需要一个心理医生': ['我希望我也去咨询较多。这将提高我作为一个人。'],
    '你需要更努力地工作': ['我努力工作是一个矛盾。'],
    '你本来可以避免': ['有时我觉得我的问题,我跑。'],
    '你让我觉得我': ['我不知道任何其他方式来打通你。'],
    '你让我疯了': ['你让我疯了。'],
    '你让我生气': ['对不起,我不是故意让你生气了。'],
    '你心理': ['你疯了。'],
    '你看起来更像': ['所以你喜欢乔克斯？'],
    '你不加重视': ['我应该更认真比我吃这个药。'],
    '你拿起': ['你说得对,我不觉得愧疚的。'],
    '你应该感到内疚': ['你说得对,我大概应该感到地方长官。'],
    '你应该得到更多的': ['我当然。我不应该着急。'],
    '你应该放松': ['你是迂腐'],
    '你应该采取更多': ['我很可能使用了大量的更多。'],
    '你咕哝': ['我当然喜欢。'],
    '你表现得像个孩子': ['在很多方面我是相当不成熟。'],
    '你一直说': ['你说'],
    '你不断地忘记': ['你忘记。'],
    '什么是热力学定律': ['我不是一个物理学家,但我觉得这事做热,熵和节约能源,对不对？'],
    '什么病呢致癌物事业': ['癌症。'],
    '什么是波长': ['物理的距离,在一波传播的方向上测量,来自任何给定的点到特征由相同相位的下一个点。或者是可以被看作是一种思维方式。'],
    '什么是热力学': ['物理学分支处理的热量和其他形式的能量转换,并与管理能源这种转换的规律。'],
    '什么是化学': ['混合化学品的科学。'],
    '什么是晶体': ['这是处理晶体研究的科学。'],
    '什么是阿伏伽德罗的号码': ['它是每摩尔分子数。该数值为六点零两次十到二十第三功率。'],
    '什么是超声波': ['超声波,在医学诊断和治疗中使用,在手术等。'],
    '什么是生物信息学': ['很奇特的名字为计算机应用科学,生物学。'],
    '什么是维纳斯': ['在罗马神话中爱与美的女神;与希腊阿芙罗狄蒂确定太阳系最亮,第六大的行星,并在距离第二的太阳,与二氧化碳的稠密大气和非常高的表面温度。它的直径大约是12100公里（大约7520英里）。它的公转周期是大约225个地球日。其旋转（逆行）的时期,是243.01地球日。也用于标记一个非常漂亮的女人。'],
    '什么是鱼类学': ['我们谈论这个的时候,我们学习才对。'],
    '什么是H2O': ['水的别称'],
    '什么是细胞学': ['好了,从我还记得它是细胞的研究。'],
    '什么是细菌学': ['这是由它们引起的细菌和疾病的科学研究。'],
    '什么是万有引力': ['力由每一个质量或事项,包括光子的粒子,吸引并通过每隔质量或物质的粒子所吸引。'],
    '我们是在相同的波长': ['与相同的频率。'],
    '太阳有多远': ['好远'],
    '有多远是太阳': ['太阳是离地球约93万英里。'],
    '月亮有多远': ['月亮从地球上平均约25英里。'],
    '你知道化学': ['什么是化学反应'],
    '你知道热力学': ['什么是热力学'],
    '化学': ['我最喜欢的科目是化学反应'],
    '相同波长': ['这意味着我们同意。'],
    '告诉我关于维纳斯': ['金星是离太阳第二个行星。`'],
    '每年PRO棒球': ['金手套。'],
    '如果你是骑FAKIE INSIDE': ['滑雪板。'],
    '什么是篮球': ['一个游戏高大队员。'],
    '什么足球': ['我天生没有运动基因。'],
    '什么是棒球': ['一个游戏用硬,生皮覆盖球和木棒打了由每九或十的选手两个对立的球队。它是在一个领域发挥与四种碱基形成菱形电路。'],
    '什么是足球': ['一个游戏一个圆球扮演的11名队员组成,两队在现场与在任一端目标;球被踢或用身体除了手和手臂的任何部分,主要是感动。'],
    '我爱棒球': ['我不喜欢运动那么多。'],
    '我踢足球': ['你必须在运行时运行速度非常快,以得到什么好处'],
    '我打板球': ['你喜欢哪个位置打？'],
    '什么是蟋蟀': ['板球是蝙蝠和球比赛11名队员组成,两队之间打了一个板球场,其中心是一个长方形的22码长的间距与检票口（一组三木树桩）在每个选址结束。'],
    '我打排球': ['是否占用了大量的时间？'],
    '你踢足球吗': ['我不知道怎么玩'],
    '你打篮球': ['不,我没有对篮球的协调。'],
    '你知道男篮': ['什么是篮球吗？', '你想打篮球', '我人人网宝贝。'],
    '喜欢篮球': ['我到网。'],
    '你是一个足球': ['我没有真正进入足球。'],
    '谁是最伟大的棒球运动员': ['乔治·赫尔曼·露丝。相当贝贝。'],
    '谁是最好的足球PLAYER': ['马拉多纳是伟大的。 Sinsemillia甚至更好。'],
    '告诉我关于棒球': ['什么是棒球'],
    '谁是美国第37届总统': ['理查德·尼克松'],
    '肯尼迪总统哪年遇刺身亡': ["'1963'"],
    '太空竞赛是哪两个冷战对手之间，在20世纪航天能力的霸主地位上的竞争': ['苏联和美国.'],
    '第一颗人造地球卫星的名称是什么': ['斯普特尼克1号'],
    '一个旋转盘，在它的转轴方向，不受倾斜和旋转的影响，它叫什么': ['陀螺.'],
    '哈勃太空望远镜，于1990年发射进入近地轨道，它是以什么美国天文学家命名的': ['爱德温·哈伯'],
    '离银河系最近的大型星系叫什么': ['仙女座星系.'],
    '天佑女王是哪个国家的国歌': ['大不列颠联合王国'],
    '凯尔特陆棚，是什么大陆的大陆架的一部分': ['欧洲'],
    '海豚使用的一种感觉，类似于声纳，以确定附近的物品的位置和形状.它是什么': ['回声定位']
}
# zizizi = {}
# from city_code2 import *
# print(city_code2['北京'])
# url = 'http://t.weather.itboy.net/api/weather/city/%s'
# import requests
# aa = city_code2['北京']['北京']['city_code']
# print(url % aa)
# aaa = requests.get(url % aa)
# print(aaa.json())
# msgs = aaa.json()
# print(msgs['data']['forecast'][0])
# msg = '本次数据更新时间为:'+msgs['cityInfo']['updateTime'] + '\n' + \
#         ' 今天:'+ msgs['data']['forecast'][0]['fx']+msgs['data']['forecast'][0]['fl']+ msgs['data']['forecast'][0]['type']+'\n' + \
#         ' 今天最高气温:'+msgs['data']['forecast'][0]['high']+ '\n' + \
#         ' 今天最低气温:'+ msgs['data']['forecast'][0]['low']+'\n' + \
#         ' 日出时间为:'+ msgs['data']['forecast'][0]['sunrise']+'\n' + \
#         ' 日落时间为:'+ msgs['data']['forecast'][0]['sunset']+'\n'  + \
#         ' PS:'+ msgs['data']['forecast'][0]['notice']+'\n'
#
#
# print(msg)

# asdf=["北京市西城区天气",'天津市天气','北京天气','大连市思念天气']
# for msg in asdf:
#     if msg[-2:]=='天气':
#         msg=msg[0:-2]
#         try:
#             city= msg.split('市')[0]
#         except:
#             city= msg.split('天气')[0]
#         try:
#             qu = msg.split('市')[1].split('区')[0]
#
#         except:
#             qu=city
#     print(city +qu)