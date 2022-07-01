import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2130_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2130_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5DDF
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_18C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_139',
    )

    ChrTalk(
        0x00FE,
        (
            '仓库里的年轻人们洗心革面\n',
            '是少数的好消息之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我在街角看见他们时\n',
            '也会打个招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这样走上正道\n',
            '就好了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_189')

    def _loc_139(): pass

    label('loc_139')

    ChrTalk(
        0x00FE,
        (
            '仓库里的年轻人们洗心革面\n',
            '是少数的好消息之一。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这样走上正道\n',
            '就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_189(): pass

    label('loc_189')

    Jump('loc_863')

    def _loc_18C(): pass

    label('loc_18C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_296',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_241',
    )

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用时，\n',
            '城里一片骚乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大惊失色的市民们\n',
            '一齐拥到协会和市长官邸……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '教区长尽力劝说\n',
            '状况才总算好了点，\n',
            '但还是有暴动会一触即发的感觉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0003)

    Jump('loc_293')

    def _loc_241(): pass

    label('loc_241')

    ChrTalk(
        0x00FE,
        (
            '导力器不能使用时，\n',
            '城里一片骚乱……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '人们仿佛连理智\n',
            '都同导力一起丢失了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_293(): pass

    label('loc_293')

    Jump('loc_863')

    def _loc_296(): pass

    label('loc_296')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_43D',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            Expr.Ez,
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_32F',
    )

    ChrTalk(
        0x00FE,
        (
            '主日学校招了准游击士\n',
            '来做讲师……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过那个人，好象连协会规章\n',
            '都记不好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉，平时要再\n',
            '努力学习一下就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43A')

    def _loc_32F(): pass

    label('loc_32F')

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B1',
    )

    ChrTalk(
        0x00FE,
        (
            '哎呀，游击士。\n',
            '前几天承蒙照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那次授课，孩子们的\n',
            '评价都很好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今后也请为王国的和平\n',
            '而努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_43A')

    def _loc_3B1(): pass

    label('loc_3B1')

    ChrTalk(
        0x00FE,
        (
            '哎呀，游击士。\n',
            '前几天承蒙照顾了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只是，后面的问题\n',
            '再努力学习一下就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像回答得不太好\n',
            '那样可没法得到孩子们的信任哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_43A(): pass

    label('loc_43A')

    Jump('loc_863')

    def _loc_43D(): pass

    label('loc_43D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_6B5',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x10)"),
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_669',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_554',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_4B0',
    )

    ChrTalk(
        0x00FE,
        (
            '诸位，\n',
            '今天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '托你们的福\n',
            '终于没让孩子们失望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_551')

    def _loc_4B0(): pass

    label('loc_4B0')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '嗯，诸位……\n',
            '今天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '托你们的福\n',
            '终于没让孩子们失望了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位游击士\n',
            '百忙之中还麻烦你们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '希望今后也能多加重视\n',
            '和地区民众的接触。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_551(): pass

    label('loc_551')

    Jump('loc_666')

    def _loc_554(): pass

    label('loc_554')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_5A4',
    )

    ChrTalk(
        0x00FE,
        (
            '诸位，\n',
            '今天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以后基础性的知识\n',
            '也请多加学习学习。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_666')

    def _loc_5A4(): pass

    label('loc_5A4')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '嗯，诸位……\n',
            '今天真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '请各位百忙之中抽空\n',
            '我也深知这样说很冒昧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但一般性的知识\n',
            '也务必要掌握啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '各位掌管着地区的治安，\n',
            '也是孩子们憧憬的对象哦。\n',
            '请不要忘记这点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_666(): pass

    label('loc_666')

    Jump('loc_6B2')

    def _loc_669(): pass

    label('loc_669')

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x00, 0x02)"),
            Expr.Return,
        ),
        'loc_67A',
    )

    Call(1, 0x0001)

    Jump('loc_6B2')

    def _loc_67A(): pass

    label('loc_67A')

    ChrTalk(
        0x00FE,
        (
            '唉，讲师\n',
            '还没好吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '再不来\n',
            '授课都要结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6B2(): pass

    label('loc_6B2')

    Jump('loc_863')

    def _loc_6B5(): pass

    label('loc_6B5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 4, 0x121C)),
            Expr.Return,
        ),
        'loc_6FC',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才开始总觉得\n',
            '外边好像吵吵嚷嚷的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是错觉吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_863')

    def _loc_6FC(): pass

    label('loc_6FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_806',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_76B',
    )

    ChrTalk(
        0x00FE,
        (
            '应该已经去找讲师了，\n',
            '但游击士那边似乎没人在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '必须赶快请求\n',
            '协会找个代替的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_803')

    def _loc_76B(): pass

    label('loc_76B')

    OP_A2(0x0003)

    ChrTalk(
        0x00FE,
        (
            '唉，真伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '应该已经去找游击士来当\n',
            '主日学校的讲师了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不凑巧那位由于工作关系\n',
            '好像不在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，必须赶快\n',
            '委托协会找个代替的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_803(): pass

    label('loc_803')

    Jump('loc_863')

    def _loc_806(): pass

    label('loc_806')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_863',
    )

    ChrTalk(
        0x00FE,
        (
            '选举运动的声音\n',
            '从这里都听得见哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '似乎会扰乱祈愿者的安宁，\n',
            '真令人感到为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_863(): pass

    label('loc_863')

    TalkEnd(0x00FE)

    Return()

# id: 0x0001 offset: 0x867
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    OP_4A(0x000D, 255)
    Fade(1000)
    SetChrPos(0x00F7, 54000, 0, 50610, 0)
    SetChrPos(0x0101, 53000, 0, 50800, 0)
    SetChrPos(0x0104, 52900, 0, 49660, 0)
    SetChrPos(0x0127, 54100, 0, 49500, 0)
    OP_8C(0x000D, 180, 0)
    OP_69(0x0101, 0x00000000)
    OP_0D()
    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_29(0x0067, 0x01, 0x8000)"),
            Expr.Return,
        ),
        'loc_923',
    )

    ChrTalk(
        0x000D,
        (
            '#2940430606V嗯，诸位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430607V讲师的工作\n',
            '可以拜托你了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A1D')

    def _loc_923(): pass

    label('loc_923')

    ChrTalk(
        0x000D,
        (
            '#2940430608V哎呀，诸位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430609V莫非你们\n',
            '是看了公告板而来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430610V#1000F啊，嗯，看了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430611V好像有要紧事\n',
            '要委托我们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430612V嗯，今天的主日学校\n',
            '想请个讲师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430613V怎么样，\n',
            '可以拜托你了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A1D(): pass

    label('loc_A1D')

    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【听工作的说明】\n'),
            TXT(0x01, '【放弃】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B20',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430614V#1007F抱歉，现在不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430615V啊，那就为难了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430616V但是没办法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430617V那么，事情办完的话\n',
            '请马上再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0067, 0x01, 0x8000)
    OP_30(0x00)
    EventEnd(0x00)

    Return()

    def _loc_B20(): pass

    label('loc_B20')

    ChrTalk(
        0x0101,
        (
            '#0010430618V#1000F嗯，没问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430619V#1015F虽然没什么自信，\n',
            '暂且试着做做看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430620V非常感谢。\n',
            '真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430621V本来委托的卡露娜小姐\n',
            '突然出差……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430622V已经是\n',
            '走投无路了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_C40',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430623V#050F原来如此啊……\n',
            '所以才这么着急吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C7A')

    def _loc_C40(): pass

    label('loc_C40')

    ChrTalk(
        0x0103,
        (
            '#0030430624V#020F原来如此呢……\n',
            '所以才这么着急的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C7A(): pass

    label('loc_C7A')

    ChrTalk(
        0x0101,
        (
            '#0010430625V#1011F……那我该\n',
            '怎么做呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430626V是，首先请到隔壁房间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430627V在那边我把授课的内容\n',
            '简单地说明一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0067, 0x04, 0x04)
    OP_28(0x0067, 0x04, 0x08)
    OP_28(0x0067, 0x01, 0x0001)
    OP_28(0x0067, 0x01, 0x0002)
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    SetChrPos(0x0101, -15920, 0, 42640, 0)
    SetChrPos(0x000D, -15920, 0, 43790, 180)
    SetChrPos(0x00F7, -16200, 0, 45190, 180)
    SetChrPos(0x0104, -17400, 0, 44260, 135)
    SetChrPos(0x0127, -17380, 0, 42570, 90)
    OP_6D(-11190, 0, 49840, 0)

    ExecExpressionWithValue(
        0x001A,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0x104, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0x104, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x001A,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0x104, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_0DD7')
    def lambda_0DD7():
        OP_69(0x001A, 0x00000BB8)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_0DD7)

    FadeIn(1500, 0)
    OP_0D()
    Sleep(1000)

    WaitForThreadExit(0x000D, 0x0001)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010430628V#1012F……原来如此呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430629V#1006F嗯，授课的方法\n',
            '我想大致能理解了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430630V从对协会手册的复习开始\n',
            '其次是游击士职务的说明……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430631V最后正确回答孩子们\n',
            '的问题就行了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430632V对，这样就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430633V那么，我就回去授课了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2940430634V结束后来叫你，\n',
            '请先在这里等候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F4A')
    def lambda_0F4A():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_0F4A')

    DispatchAsync2(0x00F7, 0x0001, lambda_0F4A)

    @scena.Lambda('lambda_0F5B')
    def lambda_0F5B():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_0F5B')

    DispatchAsync2(0x0104, 0x0001, lambda_0F5B)

    @scena.Lambda('lambda_0F6C')
    def lambda_0F6C():
        ChrTurnDirection(0x00FE, 0x000D, 400)
        Yield()

        Jump('lambda_0F6C')

    DispatchAsync2(0x0127, 0x0001, lambda_0F6C)

    OP_8B(0x000D, 0xFFFFC7CA, 0x0000B7F2, 0x0190)

    @scena.Lambda('lambda_0F8A')
    def lambda_0F8A():
        OP_6D(-14950, 0, 45890, 2000)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0F8A)

    OP_8E(0x000D, -14400, 0, 45310, 2000, 0x00)
    TerminateThread(0x00F7, 0x01)
    TerminateThread(0x0104, 0x01)
    TerminateThread(0x0127, 0x01)
    OP_8E(0x000D, -13240, 0, 47000, 2000, 0x01)
    OP_9F(0x000D, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)

    @scena.Lambda('lambda_0FE1')
    def lambda_0FE1():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000001F4)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_0FE1)

    OP_8E(0x000D, -11260, 0, 47000, 2000, 0x00)
    SetChrPos(0x000D, 48141, 1000, 50075, 180)
    OP_9F(0x000D, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000000)
    WaitForThreadExit(0x000D, 0x0002)
    Sleep(800)

    @scena.Lambda('lambda_102D')
    def lambda_102D():
        ChrTurnDirection(0x0104, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_102D)

    @scena.Lambda('lambda_103B')
    def lambda_103B():
        ChrTurnDirection(0x0127, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0127, 0x0001, lambda_103B)

    CreateThread(0x00F7, 0x01, 0x01, 0x0006)
    OP_6D(-16500, 0, 44400, 2000)
    Sleep(400)

    ChrTalk(
        0x0104,
        (
            '#0040430635V#030F嗯，不过……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430636V还真有世事难料的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_10FA',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430637V#050F呵，难得和你意见一致。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430638V我也这么想。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1147')

    def _loc_10FA(): pass

    label('loc_10FA')

    ChrTalk(
        0x0103,
        (
            '#0030430639V#027F哎呀，难得和你意见一致呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430640V我也这么想哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1147(): pass

    label('loc_1147')

    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0104, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430641V#1011F嗯？你们俩怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430642V我脸上有什么东西吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040430643V#031F呀，就算是我\n',
            '也料不到啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430644V没想到艾丝蒂尔\n',
            '竟有站上讲台的一天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0127,
        (
            '#0280430645V#151F嗯嗯，吓我一跳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_12A2',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430646V#051F啊啊，一点不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430647V这家伙比起教人\n',
            '还是更像被教的类型啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12FC')

    def _loc_12A2(): pass

    label('loc_12A2')

    ChrTalk(
        0x0103,
        (
            '#0030430648V#021F主日学校的逃课惯犯\n',
            '也成长至今了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430649V呀～姐姐真是开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12FC(): pass

    label('loc_12FC')

    OP_62(0x0101, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    OP_22(0x0031, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x00F7, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430650V#1009F有、有你们这样说话的吗～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430651V虽说确实没什么自信，\n',
            '但教教孩子们还是能行的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_13F3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050430652V#053F呼，是就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050430653V#050F……那，结束之前\n',
            '我先去小睡一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1446')

    def _loc_13F3(): pass

    label('loc_13F3')

    ChrTalk(
        0x0103,
        (
            '#0030430654V#026F是就好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430655V#020F那，结束之前\n',
            '我就休息一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1446(): pass

    label('loc_1446')

    ChrTurnDirection(0x0101, 0x0104, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430656V#1000F奥利维尔你们怎么样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040430657V#031F呼，虽然力量微薄\n',
            '也让我支持下艾丝蒂尔吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430658V这里的２楼\n',
            '能把授课看得清清楚楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0127, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x0127,
        (
            '#0280430659V#153F哦～ＮＩＣＥ　ＩＤＥＡ嘛～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0280430660V#151F我也带相机去～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    ChrTurnDirection(0x0101, 0x0127, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430661V#1019F你们两个……\n',
            '可别妨碍我哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    Sleep(1000)

    SetMapFlags(0x00400000)
    ClearChrFlags(0x0019, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_15D9',
    )

    SetChrPos(0x0103, 52248, 5000, 50355, 90)

    def _loc_15D9(): pass

    label('loc_15D9')

    SetChrPos(0x0104, 52248, 5000, 49470, 90)
    SetChrPos(0x000D, 52960, 0, 48670, 90)
    OP_4A(0x000C, 255)
    OP_4A(0x000F, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x000B, 255)
    OP_6D(52220, 5000, 48532, 0)
    OP_6B(3789, 0)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(1000)

    @scena.Lambda('lambda_1642')
    def lambda_1642():
        OP_6D(58920, 1000, 50630, 3000)

        ExitThread()

    DispatchAsync(0x001A, 0x0000, lambda_1642)

    @scena.Lambda('lambda_165A')
    def lambda_165A():
        OP_6B(2800, 3000)

        ExitThread()

    DispatchAsync(0x001A, 0x0002, lambda_165A)

    OP_6C(320000, 3000)
    WaitForThreadExit(0x001A, 0x0001)

    ChrTalk(
        0x000C,
        (
            '#2990430662V好了────',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2990430663V那么，现在开始\n',
            '由讲师来授课。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2990430664V人家特地来为大家授课，\n',
            '大家要有礼貌哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#5P是～～',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0011,
        (
            '#2P是～～',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0012,
        (
            '#2P是～～',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0010,
        (
            '#2950430668V#1P是～～',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()
    OP_8C(0x000C, 90, 400)
    OP_8E(0x000C, 61520, 1000, 52280, 2000, 0x00)
    OP_8C(0x000C, 180, 400)
    OP_6D(54420, 0, 51310, 2000)
    OP_8B(0x000D, 0x0000CA84, 0x0000C49A, 0x0190)

    ChrTalk(
        0x000D,
        (
            '#2940430669V那么，请──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x001A, 0x00, 0x01, 0x0002)
    CreateThread(0x000F, 0x00, 0x01, 0x0005)
    CreateThread(0x0011, 0x00, 0x01, 0x0005)
    CreateThread(0x0010, 0x00, 0x01, 0x0005)
    CreateThread(0x0012, 0x00, 0x01, 0x0005)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    SetChrPos(0x0101, 50390, 0, 50280, 90)

    @scena.Lambda('lambda_17E2')
    def lambda_17E2():
        ChrTurnDirection(0x000D, 0x0101, 400)
        Yield()

        Jump('lambda_17E2')

    DispatchAsync2(0x000D, 0x0001, lambda_17E2)

    @scena.Lambda('lambda_17F3')
    def lambda_17F3():
        ChrTurnDirection(0x000C, 0x0101, 400)
        Yield()

        Jump('lambda_17F3')

    DispatchAsync2(0x000C, 0x0001, lambda_17F3)

    @scena.Lambda('lambda_1804')
    def lambda_1804():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000001F4)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1804)

    OP_8E(0x0101, 56160, 1000, 50280, 2000, 0x00)
    OP_8E(0x0101, 57750, 1000, 52200, 2000, 0x00)
    OP_8E(0x0101, 58970, 1000, 52150, 2000, 0x00)
    OP_8C(0x0101, 180, 400)
    Sleep(500)

    WaitForThreadExit(0x001A, 0x0000)
    TerminateThread(0x000F, 0x00)
    TerminateThread(0x0011, 0x00)
    TerminateThread(0x0010, 0x00)
    TerminateThread(0x0012, 0x00)

    @scena.Lambda('lambda_1873')
    def lambda_1873():
        OP_8C(0x000F, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1873)

    @scena.Lambda('lambda_1881')
    def lambda_1881():
        OP_8C(0x0011, 0, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_1881)

    @scena.Lambda('lambda_188F')
    def lambda_188F():
        OP_8C(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_188F)

    OP_8C(0x0012, 315, 400)

    ChrTalk(
        0x0012,
        (
            '#2980430670V#2P姐姐，你是～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0012, 400)
    Sleep(250)

    ChrTalk(
        0x0101,
        (
            '#0010430671V#1016F这、这就自我介绍，别急哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    TerminateThread(0x000D, 0x01)
    TerminateThread(0x000C, 0x01)
    OP_8C(0x0101, 180, 400)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430672V#1018F……嗯……大家好！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430673V姐姐叫做\n',
            '艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430674V虽然还是新人，\n',
            '但也算是游击士哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0012, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0011, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0010, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#2960430675V#5P咦～是游击士～～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2980430676V#2P骗人吧，帅呆了～！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2970430677V#5P姐姐多大了～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000C, 180, 400)

    ChrTalk(
        0x000C,
        (
            '#2990430678V喂喂，待会儿才提问呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2990430679V首先让老师\n',
            '复习一下之前的内容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#2990430680V──那么，请多指教啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x000C, 0x01, 0x01, 0x0007)
    CreateThread(0x000D, 0x01, 0x01, 0x0008)
    WaitForThreadExit(0x000C, 0x0001)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 1)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010430681V#1010F唔咳…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    SetChrChipByIndex(0x0101, 65535)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#0010430682V#1006F……那，大家\n',
            '准备好了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430683V立刻开始今天\n',
            '授课中的复习吧～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)

    SetChrFlags(0x000B, 0x0080)
    OP_20(0x000003E8)
    Fade(1000)
    OP_6D(59000, 1000, 53470, 0)
    OP_67(0, 3820, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0011, 0)
    SetChrSubChip(0x0010, 0)
    SetChrSubChip(0x0012, 0)
    OP_0D()
    Sleep(400)

    OP_1D(0x19)
    Sleep(400)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '授课开始！\n',
            '～关于游击士的全部活动～',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　※选择正确的答案\n',
            '　　引导特别授课走向成功！　',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010430684V#1006F#5P首先是我的工作，\n',
            '关于游击士的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430685V游击士\n',
            '是调查和战斗的专家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430686V我们\n',
            '游击士的主要使命…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '游击士的使命是？',
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①国土的防卫与治安的保障】\n'),
            TXT(0x01, '【②地区的和平与民间人士的保护】\n'),
            TXT(0x02, '【③古代遗物的发现与封印】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1E27'),
        (0x00000001, 'loc_1F17'),
        (0x00000002, 'loc_1FF9'),
        (-1, 'loc_20F7'),
    )

    def _loc_1E27(): pass

    label('loc_1E27')

    ChrTalk(
        0x0101,
        (
            '#0010430687V#1006F#5P……是国土的防卫与治安的保障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 1)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x01, 0x000A)

    ChrTalk(
        0x0101,
        (
            '#0010430688V#1015F#5P唔……为了保卫治安\n',
            '需要抵御外敌的侵入。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430689V（感、感觉好像不大一样……\n',
            '  总、总之现在必须先继续。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)

    Jump('loc_20F7')

    def _loc_1F17(): pass

    label('loc_1F17')

    ChrTalk(
        0x0101,
        (
            '#0010430690V#1006F#5P……是地区的和平与民间人士的保护。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430691V不仅仅是击退魔兽和防止犯罪，\n',
            '还要护送物品和寻找遗失物，\n',
            '是以各种各样的形式为地区作贡献的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430692V#1001F（好！刚才表现很完美。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_20F7')

    def _loc_1FF9(): pass

    label('loc_1FF9')

    ChrTalk(
        0x0101,
        (
            '#0010430693V#1006F#5P……是古代遗物的发现与封印。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 1)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x01, 0x000A)

    ChrTalk(
        0x0101,
        (
            '#0010430694V#1008F#5P当、当然，不止是这些，\n',
            '但最近可是找到了很了不起的东西哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430695V#1007F（明、明显错误……\n',
            '  总、总之现在必须先继续。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)

    Jump('loc_20F7')

    def _loc_20F7(): pass

    label('loc_20F7')

    Call(1, 0x000C)

    ChrTalk(
        0x0101,
        (
            '#0010430696V#1000F#5P我们游击士的身份\n',
            '有正游击士和准游击士两种。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430697V其中所谓准游击士\n',
            '可以说像见习一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430698V在这时积累功绩，\n',
            '最后晋升为正游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430699V#1015F不过，成为正游击士以后\n',
            '又有另外的阶级划分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430700V被称为『Ｒａｎｋ』，\n',
            '这个阶段根据经验和实际成绩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '正游击士的Ｒａｎｋ有几等级？',
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①从Ｇ级到Ａ级共７等级】\n'),
            TXT(0x01, '【②从初级到上级共５等级】\n'),
            TXT(0x02, '【③从９级到１级共９等级】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_22F5'),
        (0x00000001, 'loc_2435'),
        (0x00000002, 'loc_24FB'),
        (-1, 'loc_2591'),
    )

    def _loc_22F5(): pass

    label('loc_22F5')

    ChrTalk(
        0x0101,
        (
            '#0010430701V#1006F#5P……从Ｇ级到Ａ级共７等级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430702V正式的阶级就这７级，\n',
            '接近升级时阶级上会附上『＋』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430703V#1015F还有更高的Ｓ级，\n',
            '不过那是建立了特殊功绩的人物\n',
            '被非正式授予的名誉阶级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430704V#1006F所以一般来说Ａ级的人\n',
            '就是最高Ｒａｎｋ的游击士了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430705V（嗯，没错吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_2591')

    def _loc_2435(): pass

    label('loc_2435')

    ChrTalk(
        0x0101,
        (
            '#0010430706V#1006F#5P……从初级到上级共５等级。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430707V#1016F#5P……很、很容易明白吧。\n',
            '虽说太土了点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430708V（太、太可疑了…………）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x01, 0x000B)
    Sleep(1000)

    Jump('loc_2591')

    def _loc_24FB(): pass

    label('loc_24FB')

    ChrTalk(
        0x0101,
        (
            '#0010430709V#1006F#5P……从９级到１级共９等级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430710V根据完成的工作\n',
            '逐渐提高等级。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430711V#1015F（咦？这不是\n',
            '说准游击士的吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2591')

    def _loc_2591(): pass

    label('loc_2591')

    Call(1, 0x000C)

    ChrTalk(
        0x0101,
        (
            '#0010430712V#1011F#5P好了，约束游击士们的组织\n',
            '是大家都知道的游击士协会。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430713V#1000F我想你们都学过了，\n',
            '协会不仅在利贝尔王国，\n',
            '在大陆的各处都有活动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430714V这个世界性组织的设立\n',
            '是在与导力革命基本同时代的…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '游击士协会成立的时间是？',
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①距今约１０年前】\n'),
            TXT(0x01, '【②距今约３０年前】\n'),
            TXT(0x02, '【③距今约５０年前】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2734'),
        (0x00000001, 'loc_27E6'),
        (0x00000002, 'loc_2896'),
        (-1, 'loc_294A'),
    )

    def _loc_2734(): pass

    label('loc_2734')

    ChrTalk(
        0x0101,
        (
            '#0010430715V#1000F#5P……距今约１０年前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x01, 0x000A)

    ChrTalk(
        0x0101,
        (
            '#0010430716V#1008F#5P好、好像意外的近呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430717V（啊……１０年前\n',
            '不是百日战役吗……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_294A')

    def _loc_27E6(): pass

    label('loc_27E6')

    ChrTalk(
        0x0101,
        (
            '#0010430718V#1000F#5P……距今约３０年前。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 1)
    Sleep(1000)

    CreateThread(0x0101, 0x01, 0x01, 0x000A)

    ChrTalk(
        0x0101,
        (
            '#0010430719V#1008F#5P比、比想象的近呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430720V（呜哇～完全没自信。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)

    Jump('loc_294A')

    def _loc_2896(): pass

    label('loc_2896')

    ChrTalk(
        0x0101,
        (
            '#0010430721V#1000F#5P……距今约５０年前。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430722V导力技术与协会渊源深厚，\n',
            '现在似乎也有受到导力器相关财团\n',
            '的资金援助哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430723V（嗯，确实是这样吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_294A')

    def _loc_294A(): pass

    label('loc_294A')

    Call(1, 0x000D)

    ChrTalk(
        0x0101,
        (
            '#0010430724V#1015F#5P嗯……接下来是游击士与\n',
            '各国关系的问题哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430725V现在，游击士协会\n',
            '在大陆全境都有设立支部……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430726V能发展壮大至此是因为\n',
            '协会是一个不与特定国家\n',
            '相关联的非政府性组织。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    SetChrChipByIndex(0x0101, 65535)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010430727V#1006F#5P但是，在实际活动中\n',
            '游击士协会也必须考虑许多东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430728V譬如为了防止与国家对立\n',
            '必须遵守一些约定俗成的规则。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430729V其中最有名的规定是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '协会与国家的约定是？',
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①与国家军队的非战斗协议】\n'),
            TXT(0x01, '【②不逮捕贵族·王族】\n'),
            TXT(0x02, '【③不干涉国家权力】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2B99'),
        (0x00000001, 'loc_2C8F'),
        (0x00000002, 'loc_2D97'),
        (-1, 'loc_2E8A'),
    )

    def _loc_2B99(): pass

    label('loc_2B99')

    ChrTalk(
        0x0101,
        (
            '#0010430730V#1000F#5P……与国家军队的非战斗协定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430731V就是说，不与那个国家\n',
            '的军队作战的协定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430732V因为在万不得已的时候\n',
            '说不定会成为敌人的组织，\n',
            '谁都不会接受的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430733V#1015F（感觉没错，\n',
            '　不过总觉得不大合适……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E8A')

    def _loc_2C8F(): pass

    label('loc_2C8F')

    ChrTalk(
        0x0101,
        (
            '#0010430734V#1002F#5P……不逮捕贵族·王族。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430735V就是说，不逮捕\n',
            '身份高贵者的协定。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430736V即使国王做了坏事\n',
            '能够裁决的也是那个国家的人民。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430737V插手他国内务\n',
            '是违反国际准则的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430738V#1015F（应该没错吧，\n',
            '　嗯～有这样的规定吗？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2E8A')

    def _loc_2D97(): pass

    label('loc_2D97')

    ChrTalk(
        0x0101,
        (
            '#0010430739V#1002F#5P……不干涉国家权力。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430740V就是说，不参与\n',
            '国家及其机关的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430741V国家内部问题，\n',
            '完全归其国民管理。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430742V插手这样的事\n',
            '是违反国际准则的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430743V#1018F（好～～说明得很顺利！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_2E8A')

    def _loc_2E8A(): pass

    label('loc_2E8A')

    Call(1, 0x000C)

    ChrTalk(
        0x0101,
        (
            '#0010430744V#1000F#5P协会就是这样以各种手段\n',
            '为国家分担大任。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430745V#1015F当然，并不是所有事情\n',
            '都是遵照规则就能很好地解决的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430746V碰上紧急事态也可能会\n',
            '处于与规则相矛盾的立场。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430747V#1002F不过这种时候，\n',
            '游击士们只要遵从原则\n',
            '来行动就可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430748V总之，我们游击士\n',
            '在任何情况下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '游击士在任何情况下都必须……？',
            TxtCtl.Enter,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①优先政府方面的判断】\n'),
            TXT(0x01, '【②优先保护民间人士】\n'),
            TXT(0x02, '【③优先与国家军队的合作】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3095'),
        (0x00000001, 'loc_3184'),
        (0x00000002, 'loc_326F'),
        (-1, 'loc_335C'),
    )

    def _loc_3095(): pass

    label('loc_3095')

    ChrTalk(
        0x0101,
        (
            '#0010430749V#1002F#5P……优先政府方面的判断。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430750V#1015F与活动地区的国家进行对立\n',
            '是必须避免的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430751V发生大事件的时候\n',
            '会变得更加重要哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430752V#1019F（虽然听起来挺象样的……\n',
            '　但规章里应该没有这条吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335C')

    def _loc_3184(): pass

    label('loc_3184')

    ChrTalk(
        0x0101,
        (
            '#0010430753V#1002F#5P……优先保护民间人士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430754V只要优先考虑这个，\n',
            '行动自然会被引向正途。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430755V不过，展开行动时\n',
            '也会出现各种问题，\n',
            '要克服这些也是必要的能力哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430756V#1006F（嗯，总结得很好！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_335C')

    def _loc_326F(): pass

    label('loc_326F')

    ChrTalk(
        0x0101,
        (
            '#0010430757V#1002F#5P……优先与国家军队的合作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430758V与国家军队的合作\n',
            '在游击士的工作里是不可或缺的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430759V相互弥补彼此的弱点，\n',
            '任何事件都能解决哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430760V#1019F（……虽说是事实、\n',
            '但规章里应该没有这条吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_335C')

    def _loc_335C(): pass

    label('loc_335C')

    Call(1, 0x000C)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430761V#1000F#5P──以上，复习到此结束了哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430762V#1001F#5P如何？　大家明白了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    Fade(1000)
    OP_6D(51560, 5000, 50610, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(400)

    CreateThread(0x0019, 0x01, 0x01, 0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_3613',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_34C2',
    )

    ChrTalk(
        0x0104,
        (
            '#0040430763V#030F#1P嗯，这样授课的前半段就结束了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430764V#031F不过，真不愧是艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430765V毫不胆怯\n',
            '教得有模有样的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3610')

    def _loc_34C2(): pass

    label('loc_34C2')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3576',
    )

    ChrTalk(
        0x0104,
        (
            '#0040430763V#030F#1P嗯，这样授课的前半段就结束了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430767V可是，就连艾丝蒂尔\n',
            '这次好像也陷入苦战了那。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430768V那么，从这里开始\n',
            '还能挽回多少呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3610')

    def _loc_3576(): pass

    label('loc_3576')

    ChrTalk(
        0x0104,
        (
            '#0040430763V#030F#1P嗯，这样授课的前半段就结束了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430770V#031F不过，真不愧是艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040430771V说得那样风马牛不相及\n',
            '居然还能如此镇定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3610(): pass

    label('loc_3610')

    Jump('loc_37A4')

    def _loc_3613(): pass

    label('loc_3613')

    ChrTalk(
        0x0104,
        (
            '#0040430772V#030F#1P嗯，这样授课的前半段就结束了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_36B0',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430773V#021F#5P呵呵，挺努力的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430774V那孩子\n',
            '什么时候学习过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37A4')

    def _loc_36B0(): pass

    label('loc_36B0')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3729',
    )

    ChrTalk(
        0x0103,
        (
            '#0030430775V#025F#5P话说回来，真是好险。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430776V那孩子真是，不知道的事\n',
            '还堂堂正正的胡编乱造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_37A4')

    def _loc_3729(): pass

    label('loc_3729')

    ChrTalk(
        0x0103,
        (
            '#0030430777V#025F#5P啊～真是看不下去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430778V那孩子大部分\n',
            '都是在胡编乱造嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030430779V真亏教区长忍得住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_37A4(): pass

    label('loc_37A4')

    OP_59()
    Sleep(400)

    Fade(1000)
    SetChrPos(0x000C, 61337, 1000, 50629, 180)
    ClearChrFlags(0x000B, 0x0080)
    OP_6D(60430, 1000, 50280, 0)
    TerminateThread(0x0019, 0x01)
    SetChrChipByIndex(0x0019, 22)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#2990430780V好～那么现在开始\n',
            '是大家期待已久的问答时间。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2990430781V如果有问题\n',
            '想问讲师，\n',
            '就尽量举手吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000C, 0x0101, 400)

    ChrTalk(
        0x000C,
        (
            '#2990430782V那么，后半段也请多指教了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x000C, 400)

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x4),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_38CC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010340921V#1006F嗯！　包在我身上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3930')

    def _loc_38CC(): pass

    label('loc_38CC')

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x3),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3904',
    )

    ChrTalk(
        0x0101,
        (
            '#0010430784V#1002F嗯，我会尽力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3930')

    def _loc_3904(): pass

    label('loc_3904')

    ChrTalk(
        0x0101,
        (
            '#0010430785V#1016F嗯、嗯，我会努力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3930(): pass

    label('loc_3930')

    CreateThread(0x000C, 0x01, 0x01, 0x0009)
    Sleep(400)

    OP_8C(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430786V#1018F好了，那么\n',
            '问答时间开始啰～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    Sleep(400)

    SetChrFlags(0x000B, 0x0080)
    Fade(1000)
    OP_6D(59000, 1000, 53470, 0)
    OP_67(0, 3820, -10000, 0)
    OP_6B(3370, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrSubChip(0x000F, 0)
    SetChrSubChip(0x0011, 0)
    SetChrSubChip(0x0010, 0)
    SetChrSubChip(0x0012, 0)
    OP_0D()
    Sleep(1000)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　问答时间开始！　\n',
            '～平日的疑问随便问～',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　※选择正确的回答\n',
            '　　突破难题！　',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_62(0x0012, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    OP_95(0x0012, 0x00000000, 0x00000000, 0x00000000, 0x00000320, 0x00002EE0)

    ChrTalk(
        0x0012,
        (
            '#2980430787V这里，这里～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 135, 400)
    CreateThread(0x0101, 0x01, 0x01, 0x000F)
    OP_6D(61300, 1000, 53470, 1500)

    ChrTalk(
        0x0101,
        (
            '#0010430788V#1018F#5P哦，真有精神啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430789V是什么问题呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2980430790V唔、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2980430791V游击士\n',
            '要多大才能当呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430792V#1006F#5P年满几岁\n',
            '才能当游击士吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430793V#1011F#5P嗯，要当游击士\n',
            '首先得当上准游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430794V考试合格就能当，\n',
            '不过要接受那个考试……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '游击士资格鉴定考试有年龄限制吗？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①没有特别的年龄限制】\n'),
            TXT(0x01, '【②条件是１６岁以上】\n'),
            TXT(0x02, '【③条件是１８岁以上】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_3CC8'),
        (0x00000001, 'loc_3DA4'),
        (0x00000002, 'loc_3EB3'),
        (-1, 'loc_3FA2'),
    )

    def _loc_3CC8(): pass

    label('loc_3CC8')

    ChrTalk(
        0x0101,
        (
            '#0010430795V#1000F#5P……没有特别的年龄限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430796V#1008F#5P但、但是，因为实力是必须的\n',
            '所以一般都是１６岁以后\n',
            '才开始接受考试哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430797V#1007F（哎哟哟……我在说什么呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3FA2')

    def _loc_3DA4(): pass

    label('loc_3DA4')

    ChrTalk(
        0x0101,
        (
            '#0010430798V#1006F#5P……条件是１６岁以上。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430799V但是，通过了考试\n',
            '也不是马上就能当上的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430800V需要暂时在游击士前辈的指导下\n',
            '进行基础性的进修才行。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430801V在那里充分地提高了实力以后\n',
            '才能成为准游击士哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430802V（顺利的回答！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_3FA2')

    def _loc_3EB3(): pass

    label('loc_3EB3')

    ChrTalk(
        0x0101,
        (
            '#0010430803V#1000F#5P……条件是１８岁以上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430804V#1008F#5P不、不过，有实力的话\n',
            '或许也能更早地接受。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430805V嗯～大概１６岁左右\n',
            '就可以了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430806V#1013F（惨了～差点误人子弟了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)

    Jump('loc_3FA2')

    def _loc_3FA2(): pass

    label('loc_3FA2')

    ChrTalk(
        0x0012,
        (
            '#2980430807V……唔～这样吗。\n',
            '到１６岁就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#2980430808V嗯，明白了。\n',
            '谢谢老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0010)
    OP_6D(59000, 1000, 53470, 1500)
    OP_62(0x0011, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    ChrTalk(
        0x0011,
        (
            '#2970430809V这里，老师。\n',
            '可以提问吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 180, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430810V#1000F#5P嗯，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2970430811V魔兽是必须\n',
            '打败不可的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#2970430812V明明也有很可爱的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430813V#1011F#5P啊，问得好。\n',
            '对付魔兽可是很困难的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430814V#1010F不过一般来说…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '应对魔兽的方法如何决定？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①根据外观判断】\n'),
            TXT(0x01, '【②必然要打倒】\n'),
            TXT(0x02, '【③重视委托人的意向】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_41E9'),
        (0x00000001, 'loc_42FA'),
        (0x00000002, 'loc_43CA'),
        (-1, 'loc_44C6'),
    )

    def _loc_41E9(): pass

    label('loc_41E9')

    ChrTalk(
        0x0101,
        (
            '#0010430815V#1010F#5P……要根据外观判断。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430816V#1008F#5P不过，其中也有\n',
            '虽然可爱但很不好对付的魔兽哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430817V因此过分依靠外观\n',
            '判断也是不行的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430818V总、总而言之\n',
            '要见机行事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430819V#1007F（乱、乱七八糟……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44C6')

    def _loc_42FA(): pass

    label('loc_42FA')

    ChrTalk(
        0x0101,
        (
            '#0010430820V#1002F#5P……必然要打倒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430821V魔兽的危险性\n',
            '与外观是没有关系的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430822V#1015F但是，也有委托人\n',
            '不希望打倒魔兽，\n',
            '而是放生的情况哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430823V（唔～应该有\n',
            '更好的答法……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_44C6')

    def _loc_43CA(): pass

    label('loc_43CA')

    ChrTalk(
        0x0101,
        (
            '#0010430824V#1000F#5P……要重视委托人的意向。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430825V应对魔兽的方法是没有标准答案的。\n',
            '必须见机行事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430826V所以，在委托人\n',
            '不希望打倒魔兽的情况下，\n',
            '也有可能会放生哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430827V#1006F（虽然是个难题\n',
            '但看来回答得不错。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_44C6')

    def _loc_44C6(): pass

    label('loc_44C6')

    ChrTalk(
        0x0011,
        (
            '#2970430828V哦～原来如此啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    ChrTalk(
        0x0010,
        (
            '#2950430829V我也可以提问吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430830V#1000F#5P嗯，可以呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x01, 0x0011)
    OP_6D(57600, 1000, 53470, 1500)

    ChrTalk(
        0x0010,
        (
            '#2950430831V前阵子有发生空贼团\n',
            '袭击定期船的事件吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2950430832V那时逮捕空贼的\n',
            '是王国军的士兵们？\n',
            '还是游击士们？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430833V#1011F#5P定期船『林德号』\n',
            '被袭击的事件吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430834V#1015F那时最后\n',
            '逮捕了空贼团的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '逮捕了空贼团卡普亚一家的是？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①当然是游击士】\n'),
            TXT(0x01, '【②是王国军的部队】\n'),
            TXT(0x02, '【③是亲卫队的队员】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_46FB'),
        (0x00000001, 'loc_4818'),
        (0x00000002, 'loc_4928'),
        (-1, 'loc_4A65'),
    )

    def _loc_46FB(): pass

    label('loc_46FB')

    ChrTalk(
        0x0101,
        (
            '#0010430835V#1012F#5P……当然是游击士。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430836V#1008F#5P啊，不过突击作战\n',
            '是和王国军配合进行的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430837V……抱、抱歉\n',
            '稍微有点记忆混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430838V#1015F总、总之是游击士和王国军\n',
            '齐心协力逮捕的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430839V（呜～是哪一个来着……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A65')

    def _loc_4818(): pass

    label('loc_4818')

    ChrTalk(
        0x0101,
        (
            '#0010430840V#1000F#5P……是王国军的部队。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430841V最后的突击作战，\n',
            '游击士和王国军形成\n',
            '将空贼两面夹击之势。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430842V空贼逃跑时\n',
            '王国军赶到将其逮捕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430843V就是说，是游击士和王国军\n',
            '齐心协力逮捕到的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430844V#1006F（好，没问题吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_4A65')

    def _loc_4928(): pass

    label('loc_4928')

    ChrTalk(
        0x0101,
        (
            '#0010430845V#1000F#5P……是亲卫队的队员。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430846V#1015F#5P咦，不过那个时候\n',
            '亲卫队好像是不在的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430847V#1013F……抱、抱歉\n',
            '稍微有点记忆混乱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430848V总、总之是游击士和王国军\n',
            '齐心协力逮捕的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430849V#1007F（亲卫队出现是在\n',
            '逮捕戴尔蒙市长的时候吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4A65')

    def _loc_4A65(): pass

    label('loc_4A65')

    ChrTalk(
        0x0010,
        (
            '#2950430850V是吗，是王国军\n',
            '与游击士合力抓到的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#2950430851V嗯，这是最重要的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Call(1, 0x0010)
    ClearChrFlags(0x001B, 0x0080)

    @scena.Lambda('lambda_4AD1')
    def lambda_4AD1():
        OP_8F(0x001B, 56350, 0, 44730, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_4AD1)

    OP_6D(59000, 1000, 53470, 1500)

    ChrTalk(
        0x001B,
        (
            '#3000430852V#1P请问～～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430853V#1P可以提问吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0101, 0x01, 0x01, 0x0012)
    OP_6D(57260, 1000, 50270, 1500)
    ChrTurnDirection(0x0101, 0x001B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010430854V#1000F好的，请说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430855V#1P我正在准备考试\n',
            '不过忘记了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430856V#1P『对民间人士的保护义务』\n',
            '是协会规章的第几项？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430857V#1004F（唔唔…………！？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430858V（这、这怎么\n',
            '可能背得下来嘛！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 1)
    Sleep(600)

    ChrTalk(
        0x0101,
        (
            '#0010430859V#1015F稍、稍等一下，\n',
            '『对民间人士的保护义务』对吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430860V唔、嗯～那个大概……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '『对民间人士的保护义务』是第几项？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①协会规章第一项】\n'),
            TXT(0x01, '【②协会规章第二项】\n'),
            TXT(0x02, '【③协会规章第三项】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    Sleep(400)

    SetChrChipByIndex(0x0101, 65535)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4DB9'),
        (0x00000001, 'loc_4F41'),
        (0x00000002, 'loc_5019'),
        (-1, 'loc_51A3'),
    )

    def _loc_4DB9(): pass

    label('loc_4DB9')

    ChrTalk(
        0x0101,
        (
            '#0010430861V#1015F……协会规章第一项，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430862V#1P咦……是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430863V#1P第一项不是『基本理念』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430864V#1008F哎，咦……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430865V#1P啊，不好意思。\n',
            '我自己想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430866V#1P『对民间人士的保护』是第二项吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430867V#1016F想、想起来就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430868V#1007F（真、真没面子～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51A3')

    def _loc_4F41(): pass

    label('loc_4F41')

    ChrTalk(
        0x0101,
        (
            '#0010430869V#1015F……协会规章第二项，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430870V#1P啊，对了。\n',
            '我现在也想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430871V#1P谢谢您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430872V#1016F哪里，不客气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430873V（呼～总算撑过去了。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_51A3')

    def _loc_5019(): pass

    label('loc_5019')

    ChrTalk(
        0x0101,
        (
            '#0010430874V#1000F……协会规章第三项，是吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430875V#1P嗯……是这样吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430876V#1P第三项不是『不干涉国家』吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430864V#1008F哎，咦……是吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430865V#1P啊，不好意思。\n',
            '我自己想起来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#3000430866V#1P『对民间人士的保护』是第二项吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430867V#1016F想、想起来就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430868V#1007F（真、真没面子～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51A3')

    def _loc_51A3(): pass

    label('loc_51A3')

    CreateThread(0x0101, 0x01, 0x01, 0x0010)
    OP_6D(59000, 1000, 53470, 1500)

    @scena.Lambda('lambda_51C1')
    def lambda_51C1():
        OP_8F(0x001B, 56350, -600, 44730, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_51C1)

    ChrTalk(
        0x0101,
        (
            '#0010430882V#1000F……嗯……还有别的问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x001B, 0x0001)
    SetChrFlags(0x001B, 0x0080)

    ChrTalk(
        0x000F,
        (
            '#2960430883V#2P那么，请问老师。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430884V#1000F#5P嗯，什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430885V#2P那个，和今天的授课\n',
            '虽然没多大关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430886V#2P逮捕市长的时候，\n',
            '女王陛下的飞船来了对吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430887V#2P那艘飞船……\n',
            '有多大？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430888V#1019F#5P（来、来了……\n',
            '完全不合时宜的问题。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0011350037V#1016F……嗯……女王陛下的飞船\n',
            '是说埃尔赛尤号吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430889V#2P嗯，就是那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430890V#2P看起来好像非常大，\n',
            '到底有多大呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010430891V#1015F#5P埃尔赛尤的大小啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430892V嗯～记得之前在什么书上\n',
            '看到过似的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetMessageWindowPos(-1, 16, -1, -1)

    Talk(
        (
            0x18,
            '埃尔赛尤号的全长是？',
            TxtCtl.Enter,
        ),
    )

    Menu(
        0,
        -1,
        150,
        0,
        (
            TXT(0x00, '【①全长２２亚矩】\n'),
            TXT(0x01, '【②全长３２亚矩】\n'),
            TXT(0x02, '【③全长４２亚矩】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_5500'),
        (0x00000001, 'loc_55FE'),
        (0x00000002, 'loc_56FC'),
        (-1, 'loc_5796'),
    )

    def _loc_5500(): pass

    label('loc_5500')

    ChrTalk(
        0x0101,
        (
            '#0010430893V#1015F#5P……全长２２亚矩吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 1)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430894V#1007F#5P抱、抱歉……\n',
            '说实话我也没什么自信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430895V说不定搞错了，\n',
            '大家还是查查书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430896V是吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430897V那么，还是去看书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5796')

    def _loc_55FE(): pass

    label('loc_55FE')

    ChrTalk(
        0x0101,
        (
            '#0010430898V#1015F#5P……全长３２亚矩吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 1)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010430894V#1007F#5P抱、抱歉……\n',
            '说实话我也没什么自信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430895V说不定搞错了，\n',
            '大家还是查查书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430896V是吗～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430897V那么，还是去看书吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5796')

    def _loc_56FC(): pass

    label('loc_56FC')

    ChrTalk(
        0x0101,
        (
            '#0010430903V#1015F#5P我记得……\n',
            '全长是４２亚矩吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010430904V不一定完全正确\n',
            '不过大体上应该差不多吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#2960430905V咦～果然好大。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithReg(
        0x0002,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Jump('loc_5796')

    def _loc_5796(): pass

    label('loc_5796')

    ChrTalk(
        0x000F,
        (
            '#2960430906V谢谢～老师～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetChrPos(0x000C, 61337, 1000, 50629, 180)
    OP_6D(58920, 1000, 50630, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    SetChrChipByIndex(0x0101, 65535)
    ClearChrFlags(0x000B, 0x0080)
    FadeIn(1500, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(
        0x000C,
        (
            '#2990430907V──好了，没有问题了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2990430908V……好，那么到这里\n',
            '老师的授课就结束啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2990430909V好了，对老师说声谢谢吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 200, -1, -1)
    SetChrName('孩子们')

    Talk(
        (
            '#2960430910V谢谢～老师～',
            TxtCtl.Enter,
        ),
    )

    OP_56(0x01)
    OP_59()

    ChrTalk(
        0x0101,
        (
            '#0010430911V#1001F那么，再见喽～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0x7),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_5956',
    )

    If(
        (
            (Expr.PushReg, 0x2),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5948',
    )

    OP_2B(0x0067, 0x0002)
    OP_2C(0x0067, 0x03E8)
    OP_28(0x0067, 0x01, 0x2000)
    OP_28(0x0067, 0x01, 0x0004)

    Jump('loc_594E')

    def _loc_5948(): pass

    label('loc_5948')

    OP_28(0x0067, 0x01, 0x0008)

    def _loc_594E(): pass

    label('loc_594E')

    OP_28(0x0067, 0x04, 0x10)

    Jump('loc_596C')

    def _loc_5956(): pass

    label('loc_5956')

    OP_28(0x0067, 0x01, 0x4000)
    OP_28(0x0067, 0x01, 0x0010)
    OP_28(0x0067, 0x04, 0x40)
    OP_28(0x0067, 0x04, 0x80)
    def _loc_596C(): pass

    label('loc_596C')

    ClearMapFlags(0x00400000)
    OP_A2(0x10F2)
    NewScene('ED6_DT21/T2100._SN', 105, 0, 0)
    IdleLoop()

    Return()

# id: 0x0002 offset: 0x597E
@scena.Code('ReInit')
def ReInit():
    OP_6D(58920, 1000, 50630, 3000)

    Return()

# id: 0x0003 offset: 0x5990
@scena.Code('func_03_5990')
def func_03_5990():
    OP_6B(2800, 4000)

    Return()

# id: 0x0004 offset: 0x599A
@scena.Code('func_04_599A')
def func_04_599A():
    SetChrPos(0x001A, 57760, 0, 48830, 0)
    OP_69(0x001A, 0x00000FA0)

    Return()

# id: 0x0005 offset: 0x59B3
@scena.Code('func_05_59B3')
def func_05_59B3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5A6E',
    )

    Switch(
        (
            Expr.Rand,
            (Expr.PushLong, 0x4),
            Expr.Mod,
            Expr.Return,
        ),
        (0x00000000, 'loc_59D9'),
        (0x00000001, 'loc_59E1'),
        (0x00000002, 'loc_59E9'),
        (0x00000003, 'loc_59F1'),
        (-1, 'loc_59F9'),
    )

    def _loc_59D9(): pass

    label('loc_59D9')

    Sleep(200)

    Jump('loc_59F9')

    def _loc_59E1(): pass

    label('loc_59E1')

    Sleep(300)

    Jump('loc_59F9')

    def _loc_59E9(): pass

    label('loc_59E9')

    Sleep(400)

    Jump('loc_59F9')

    def _loc_59F1(): pass

    label('loc_59F1')

    Sleep(500)

    Jump('loc_59F9')

    def _loc_59F9(): pass

    label('loc_59F9')

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x3),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5A1C',
    )

    OP_62(0x00FE, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)

    def _loc_5A1C(): pass

    label('loc_5A1C')

    Switch(
        (
            Expr.Rand,
            (Expr.PushLong, 0x6),
            Expr.Mod,
            Expr.Return,
        ),
        (0x00000000, 'loc_5A39'),
        (0x00000001, 'loc_5A43'),
        (0x00000002, 'loc_5A4D'),
        (0x00000003, 'loc_5A57'),
        (-1, 'loc_5A61'),
    )

    def _loc_5A39(): pass

    label('loc_5A39')

    OP_8C(0x00FE, 45, 400)

    Jump('loc_5A6B')

    def _loc_5A43(): pass

    label('loc_5A43')

    OP_8C(0x00FE, 90, 400)

    Jump('loc_5A6B')

    def _loc_5A4D(): pass

    label('loc_5A4D')

    OP_8C(0x00FE, 315, 400)

    Jump('loc_5A6B')

    def _loc_5A57(): pass

    label('loc_5A57')

    OP_8C(0x00FE, 270, 400)

    Jump('loc_5A6B')

    def _loc_5A61(): pass

    label('loc_5A61')

    OP_8C(0x00FE, 0, 400)

    Jump('loc_5A6B')

    def _loc_5A6B(): pass

    label('loc_5A6B')

    Jump('func_05_59B3')

    def _loc_5A6E(): pass

    label('loc_5A6E')

    Return()

# id: 0x0006 offset: 0x5A6F
@scena.Code('func_06_5A6F')
def func_06_5A6F():
    OP_8E(0x00F7, -15920, 0, 44780, 1000, 0x00)
    ChrTurnDirection(0x00F7, 0x0101, 400)

    Return()

# id: 0x0007 offset: 0x5A8B
@scena.Code('func_07_5A8B')
def func_07_5A8B():
    OP_8E(0x000C, 63560, 0, 52120, 2000, 0x00)
    OP_8E(0x000C, 63630, 0, 50350, 2000, 0x00)
    OP_8E(0x000C, 65500, 0, 50340, 2000, 0x00)
    OP_8C(0x000C, 270, 400)

    Return()

# id: 0x0008 offset: 0x5ACF
@scena.Code('func_08_5ACF')
def func_08_5ACF():
    Sleep(800)

    OP_8E(0x000D, 53030, 0, 46150, 2000, 0x00)
    OP_8C(0x000D, 90, 400)

    Return()

# id: 0x0009 offset: 0x5AF0
@scena.Code('func_09_5AF0')
def func_09_5AF0():
    OP_8E(0x000C, 65500, 0, 50340, 2000, 0x00)
    OP_8C(0x000C, 270, 400)

    Return()

# id: 0x000A offset: 0x5B0C
@scena.Code('func_0A_5B0C')
def func_0A_5B0C():
    OP_62(0x0010, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0011, 0x000F, 400)
    Sleep(400)

    OP_62(0x0011, 0x00000000, 1700, 0x00, 0x01, 0x000000FA, 0x02)
    OP_22(0x0026, 0x00, 0x64)
    ChrTurnDirection(0x000F, 0x0011, 400)
    Sleep(2000)

    OP_8C(0x0011, 0, 400)
    OP_8C(0x000F, 0, 400)

    Return()

# id: 0x000B offset: 0x5B66
@scena.Code('func_0B_5B66')
def func_0B_5B66():
    OP_62(0x0010, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0011, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    OP_62(0x000F, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0012, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    OP_22(0x0031, 0x00, 0x64)

    Return()

# id: 0x000C offset: 0x5BCD
@scena.Code('func_0C_5BCD')
def func_0C_5BCD():
    Sleep(400)

    FadeOut(600, 0, -1)
    OP_0D()
    Sleep(800)

    FadeIn(600, 0)
    OP_0D()

    Return()

# id: 0x000D offset: 0x5BED
@scena.Code('func_0D_5BED')
def func_0D_5BED():
    Sleep(400)

    FadeOut(600, 0, -1)
    OP_0D()
    Sleep(800)

    SetChrChipByIndex(0x0101, 10)
    SetChrSubChip(0x0101, 1)
    FadeIn(600, 0)
    OP_0D()

    Return()

# id: 0x000E offset: 0x5C17
@scena.Code('func_0E_5C17')
def func_0E_5C17():
    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    def _loc_5C2B(): pass

    label('loc_5C2B')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CC8',
    )

    Sleep(600)

    SetChrChipByIndex(0x0019, 25)
    Sleep(600)

    def _loc_5C43(): pass

    label('loc_5C43')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CB6',
    )

    LoadEffect(0x00, 'map\\\\mp032_00.eff')
    OP_22(0x007C, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x0019, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x2),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5CB3',
    )

    Jump('loc_5CB6')

    def _loc_5CB3(): pass

    label('loc_5CB3')

    Jump('loc_5C43')

    def _loc_5CB6(): pass

    label('loc_5CB6')

    Sleep(1000)

    SetChrChipByIndex(0x0019, 22)
    Sleep(1000)

    Jump('loc_5C2B')

    def _loc_5CC8(): pass

    label('loc_5CC8')

    Return()

# id: 0x000F offset: 0x5CC9
@scena.Code('func_0F_5CC9')
def func_0F_5CC9():
    @scena.Lambda('lambda_5CCF')
    def lambda_5CCF():
        ChrTurnDirection(0x0010, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5CCF)

    Sleep(100)

    @scena.Lambda('lambda_5CE2')
    def lambda_5CE2():
        ChrTurnDirection(0x0011, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5CE2)

    Sleep(50)

    @scena.Lambda('lambda_5CF5')
    def lambda_5CF5():
        ChrTurnDirection(0x000F, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5CF5)

    Return()

# id: 0x0010 offset: 0x5CFE
@scena.Code('func_10_5CFE')
def func_10_5CFE():
    @scena.Lambda('lambda_5D04')
    def lambda_5D04():
        OP_8C(0x0010, 0, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5D04)

    Sleep(100)

    @scena.Lambda('lambda_5D17')
    def lambda_5D17():
        OP_8C(0x0011, 0, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5D17)

    @scena.Lambda('lambda_5D25')
    def lambda_5D25():
        OP_8C(0x0012, 315, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_5D25)

    Sleep(50)

    @scena.Lambda('lambda_5D38')
    def lambda_5D38():
        OP_8C(0x000F, 0, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5D38)

    Return()

# id: 0x0011 offset: 0x5D41
@scena.Code('func_11_5D41')
def func_11_5D41():
    @scena.Lambda('lambda_5D47')
    def lambda_5D47():
        ChrTurnDirection(0x0012, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_5D47)

    Sleep(100)

    @scena.Lambda('lambda_5D5A')
    def lambda_5D5A():
        ChrTurnDirection(0x0011, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5D5A)

    Sleep(50)

    @scena.Lambda('lambda_5D6D')
    def lambda_5D6D():
        ChrTurnDirection(0x000F, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5D6D)

    Return()

# id: 0x0012 offset: 0x5D76
@scena.Code('func_12_5D76')
def func_12_5D76():
    @scena.Lambda('lambda_5D7C')
    def lambda_5D7C():
        ChrTurnDirection(0x0012, 0x001B, 400)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_5D7C)

    Sleep(100)

    @scena.Lambda('lambda_5D8F')
    def lambda_5D8F():
        ChrTurnDirection(0x0011, 0x001B, 400)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_5D8F)

    Sleep(50)

    @scena.Lambda('lambda_5DA2')
    def lambda_5DA2():
        ChrTurnDirection(0x000F, 0x001B, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_5DA2)

    @scena.Lambda('lambda_5DB0')
    def lambda_5DB0():
        ChrTurnDirection(0x0010, 0x001B, 400)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_5DB0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
