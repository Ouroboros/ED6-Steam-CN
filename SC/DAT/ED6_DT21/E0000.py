import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import E0000_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('E0000   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'event'
    header.mapModel       = 'E0000.x'
    header.mapIndex       = 1
    header.bgm            = 1
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000FA0,
            dword_08        = 0xFFFFEE6C,
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01660._CH', 'ED6_DT07/CH01660P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '森特',
            x                   = -3050,
            z                   = 5000,
            y                   = 8470,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = -1600,
            z                   = 5000,
            y                   = -4820,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0111,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '乘客',
            x                   = -3510,
            z                   = 5000,
            y                   = -4010,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x122
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x122
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 5, 0x1205)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_133',
    )

    MapSetFlags(0x10000000)
    Event(0, func_06_57C)

    def _loc_133(): pass

    label('loc_133')

    Return()

# id: 0x0001 offset: 0x134
@scena.Code('func_01_134')
def func_01_134():
    PlaySE(121, 0x01, 0x46)
    PlaySE(451, 0x00, 0x64)

    Return()

# id: 0x0002 offset: 0x13F
@scena.Code('func_02_13F')
def func_02_13F():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_164',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_2A6')

    def _loc_164(): pass

    label('loc_164')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_17D',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_2A6')

    def _loc_17D(): pass

    label('loc_17D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_196',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_2A6')

    def _loc_196(): pass

    label('loc_196')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AF',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_2A6')

    def _loc_1AF(): pass

    label('loc_1AF')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1C8',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_2A6')

    def _loc_1C8(): pass

    label('loc_1C8')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1E1',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_2A6')

    def _loc_1E1(): pass

    label('loc_1E1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1FA',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_2A6')

    def _loc_1FA(): pass

    label('loc_1FA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_213',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_2A6')

    def _loc_213(): pass

    label('loc_213')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_22C',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_2A6')

    def _loc_22C(): pass

    label('loc_22C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_245',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_2A6')

    def _loc_245(): pass

    label('loc_245')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25E',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_2A6')

    def _loc_25E(): pass

    label('loc_25E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_277',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_2A6')

    def _loc_277(): pass

    label('loc_277')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_290',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_2A6')

    def _loc_290(): pass

    label('loc_290')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A6',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_2A6(): pass

    label('loc_2A6')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2BB',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_2A6')

    def _loc_2BB(): pass

    label('loc_2BB')

    Return()

# id: 0x0003 offset: 0x2BC
@scena.Code('func_03_2BC')
def func_03_2BC():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0241, 3, 0x120B)),
            Expr.Return,
        ),
        'loc_364',
    )

    ChrTalk(
        0x00FE,
        (
            '我现在要去调查\n',
            '位于卢安的『绀碧之塔』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实诞辰庆典的时候，\n',
            '就有人在『四轮之塔』目睹到了奇怪的现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但事后隔了很久，\n',
            '才有人对其展开调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_455')

    def _loc_364(): pass

    label('loc_364')

    SetScenaFlags(ScenaFlag(0x0241, 3, 0x120B))

    ChrTalk(
        0x00FE,
        (
            '呼，真遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天的云好像很多，\n',
            '看不见『绀碧之塔』呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是历史资料馆的研究员。\n',
            '正准备去绀碧之塔做实地调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实诞辰庆典的时候，\n',
            '就有人在『四轮之塔』目睹到了奇怪的现象……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但事后隔了很久，\n',
            '才有人对其展开调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_455(): pass

    label('loc_455')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x459
@scena.Code('func_04_459')
def func_04_459():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4B5',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，小孩子就是天不怕地不怕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我光是站在这个地方，\n',
            '双腿就开始发软了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4EC')

    def _loc_4B5(): pass

    label('loc_4B5')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '喂，喂喂。\n',
            '别去那边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '掉下去怎么办。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x00FE, 0x0010)

    def _loc_4EC(): pass

    label('loc_4EC')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x4F0
@scena.Code('func_05_4F0')
def func_05_4F0():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_540',
    )

    ChrTalk(
        0x00FE,
        (
            '喂，爸爸也来这边嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那些山啊河啊，\n',
            '全部都看起来好小哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_578')

    def _loc_540(): pass

    label('loc_540')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哇，真厉害。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿，看啊！\n',
            '树木变得那么小了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_578(): pass

    label('loc_578')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x57C
@scena.Code('func_06_57C')
def func_06_57C():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_58F',
    )

    Call(0, 0x0007)

    def _loc_58F(): pass

    label('loc_58F')

    OP_12(0x0001ADB0, 0x000249F0, 0x00000000)
    CameraMove(600, 5000, 44810, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(7230, 0)
    OP_6C(143000, 0)
    OP_6E(332, 0)
    ChrSetPos(0x0101, 3260, 5000, -4580, 85)
    ChrSetPos(0x00F7, 3270, 5000, -3730, 101)
    OP_12(0x00009C40, 0x0001ADB0, 0x000032C8)
    OP_C8(0x0080, 0x0046, 'C_PLAC29._CH', 0x00, 0x07D0)
    FadeIn(2000, 0)

    @scena.Lambda('lambda_062C')
    def lambda_062C():
        CameraMove(4040, 5000, -3270, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_062C)

    @scena.Lambda('lambda_0644')
    def lambda_0644():
        OP_67(0, 10000, -10000, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0644)

    @scena.Lambda('lambda_065C')
    def lambda_065C():
        CameraSetDistance(3500, 11000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_065C)

    Sleep(4000)

    @scena.Lambda('lambda_0671')
    def lambda_0671():
        OP_6C(53000, 7000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0671)

    WaitForThreadExit(0x0101, 0x0001)
    Fade(1000)
    CameraMove(4040, 5000, -3270, 0)
    OP_67(0, 10000, -10000, 0)
    CameraSetDistance(2140, 0)
    OP_6C(53000, 0)
    OP_6E(332, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_10A6',
    )

    ChrTalk(
        0x0101,
        (
            '#0010200581V#1011F嗯嗯，天气真好啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200582V照这么看来，\n',
            '今天卢安地区应该很适合观光吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200583V#5P#051F或许吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200584V不过现在，因为观光之外的事情\n',
            '这里变得十分热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200585V#1004F观光之外的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050200586V#5P#053F就是市长选举。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200587V为了取代先前被捕的戴尔蒙，\n',
            '好像有两个候选人进行角逐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200588V#1011F噢～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200589V#1015F不过，确实也该这么做呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200590V毕竟一个城市应该不可能\n',
            '永远都没有市长来管理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200591V#5P#051F说起来，\n',
            '那起事件是由你们解决的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200592V之后我问过嘉恩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191053V#1016F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200594V#1008F嗯，阿加特离开之后，\n',
            '就剩下我和约修亚，还有科洛丝了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200595V不过，幸好得到了记者他们的帮助，\n',
            '亲卫队最后将市长逮捕了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200596V#5P#051F哼。成功不是单靠一个人的，\n',
            '你能明白这点也算是进步了不少。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200597V#551F话说回来，没想到那个\n',
            '穿校服的女孩竟然是科洛蒂娅公主……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200598V在王城知道她真正身份的时候，\n',
            '就连我也吓了一大跳啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200599V#1016F啊哈哈，你这种心情我能理解。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200600V#1015F说到这个，自从诞辰庆典结束后\n',
            '就没见过科洛丝和奥利维尔了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200601V#1003F嗯嗯，提妲、博士，\n',
            '还有金先生他们也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200602V#5P#552F其实之前我向提妲和老爷子\n',
            '提过你和约修亚的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200603V可以看得出来，\n',
            '他们两个非常担心你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200604V#1025F是这样啊……\n',
            '谢谢你，阿加特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200605V#5P#053F总之，有机会的话，\n',
            '还是写封信直接问候他们一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200606V#050F金那家伙，\n',
            '诞辰庆典之后就回卡尔瓦德了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200607V不过，他出发前也叫我代他向你们问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200608V#1025F是吗……\n',
            '真想亲自向他打招呼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200609V#5P#051F话说回来，\n',
            '公主似乎已经回到学院继续念书了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200610V反正我们难得去一趟卢安。\n',
            '有空的话就去学校打个招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200611V#1016F嗯，说得也是。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200612V#1008F呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050200613V#5P#055F干、干嘛。\n',
            '我说错话了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200614V#1012F不，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200615V#1017F只是我没有想到\n',
            '阿加特有时候也懂得体贴他人呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200616V像是在王都准备出发的时候\n',
            '也叮嘱过我要做好准备之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2300, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0106,
        (
            '#0050200617V#5P#552F别、别说些无聊的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200618V#050F真是的……\n',
            '到达卢安之前我要在座位上睡觉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050200619V你就在飞船内闲逛好了，\n',
            '但是别忘了到卢安之后要下船哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 315, 400)

    @scena.Lambda('lambda_0F83')
    def lambda_0F83():
        CameraMove(1540, 5000, -2430, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0F83)

    @scena.Lambda('lambda_0F9B')
    def lambda_0F9B():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_0F9B)

    ChrWalkTo(0x0106, -30, 5100, -1630, 2000, 0x00)
    ChrSetDirection(0x0106, 14, 400)
    Sleep(500)

    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    PlaySE(6, 0x00, 0x64)
    OP_73(0x0000)

    @scena.Lambda('lambda_0FE6')
    def lambda_0FE6():
        ChrTurnDirection(0x0101, 0x0106, 0)
        Yield()

        Jump('lambda_0FE6')

    DispatchAsync2(0x0101, 0x0000, lambda_0FE6)

    ChrWalkTo(0x0106, -30, 5100, 270, 2000, 0x00)
    OP_6F(0x0000, 59)
    OP_70(0x0000, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)

    ChrTalk(
        0x0101,
        (
            '#0010200620V#1016F真是的……\n',
            '说话还是这么不饶人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200621V#1006F那么，在抵达之前还有空闲时间，\n',
            '不如在船里逛逛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x00)
    FormationDelMember(0x05, 0xFF)

    Jump('loc_1C5F')

    def _loc_10A6(): pass

    label('loc_10A6')

    ChrTalk(
        0x0101,
        (
            '#0010200581V#1011F嗯嗯，天气真好啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200582V照这么看来，\n',
            '今天卢安地区应该很适合观光吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200624V#5P#021F呵呵，或许吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200625V#020F不过现在的卢安市\n',
            '好像在为观光之外的事情而狂热。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010200585V#1004F观光之外的事情？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030200627V#5P#020F就是市长选举哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200628V前任市长被逮捕已经有一段时间，\n',
            '如今终于举行新市长的选举了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200629V而且，据说两名旗鼓相当的候选人\n',
            '已经展开了激烈的选举战。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200588V#1011F噢～是这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200589V#1015F不过确实也该这么做呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200590V毕竟一个城市应该不可能\n',
            '永远都没有市长来管理吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200633V#5P#023F哎呀，说到这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200634V我记得前任市长戴尔蒙被逮捕事件\n',
            '好像和你们有关吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191053V#1016F啊、啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200636V#1008F嗯，其实是在调查其它事件时，\n',
            '偶然发现市长其实也有所牵连的缘故。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200637V不过，我们之所以能逮捕到市长，\n',
            '全是因为科洛丝和亲卫队的帮忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200638V#5P#021F呵呵，你还真谦虚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200639V能看到自己的学生表现得如此出色，\n',
            '作为教官的我也感到很自豪哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200640V#020F不过，是这样的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200641V你们和科洛蒂娅公主\n',
            '就是在那个时候认识的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200642V#1000F嗯，没错。\n',
            '是和约修亚一起帮忙准备学院祭的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200643V#1015F说起来，自从诞辰庆典结束之后，\n',
            '我们再也没和科洛丝他们见过面了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200601V#1003F呼呼，提妲，博士，\n',
            '还有金先生他们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200645V#5P#020F金先生在\n',
            '诞辰庆典之后就回到卡尔瓦德了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200646V好像是因为接到了来自\n',
            '共和国协会的回国请求。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200647V他回国前拜托过我代他向你们问好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200648V#1007F是吗……\n',
            '他有工作在身，没办法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200649V#1025F毕竟金先生帮了我们这么多，\n',
            '真想亲自跟他打声招呼呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200650V#5P#020F将来总会有机会的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200651V而至于提妲和\n',
            '拉赛尔博士……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200652V我和卡西乌斯老师已经向他们\n',
            '简单说明了你和约修亚的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200653V#1025F是这样啊……\n',
            '谢谢你，雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200654V#5P#021F呵呵，说起来，\n',
            '提妲真是个善良体贴的孩子呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200655V#027F听了我们的话之后，\n',
            '她的眼眶一下子变得泪汪汪的，\n',
            '还强忍着泪水说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200656V『姐姐她现在正在努力，\n',
            '  所以我也不能够哭。』\n',
            '她是这样说的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200657V#1008F啊，啊哈哈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200658V#1013F那个孩子真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200659V#1027F真是的……\n',
            '雪拉姐，别逗我哭啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200660V#5P#021F抱歉抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200661V#027F不过说真的，\n',
            '你们两人遇到了很多知心的好朋友呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200662V所以，好好珍惜这份友情吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200663V#1012F嗯……我知道的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200664V#1017F对了，雪拉姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200665V我们到了卢安地区之后，\n',
            '可不可以一边工作一边去向\n',
            '曾经帮助过我们的朋友问好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200666V#5P#021F嗯，当然可以了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200667V#020F那么……\n',
            '距离抵达还有一段时间呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200668V我想在座位上小睡一会儿，\n',
            '你打算做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200669V#1015F嗯，这样啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010200670V#1011F我倒是想在定期船里面散散步，\n',
            '那我就先走了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030200671V#5P#020F嗯，我知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030200672V但是，千万别忘记\n',
            '我们要在卢安下飞船哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x00F7, 315, 400)

    @scena.Lambda('lambda_1BBB')
    def lambda_1BBB():
        CameraMove(1540, 5000, -2430, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_1BBB)

    @scena.Lambda('lambda_1BD3')
    def lambda_1BD3():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x00F7, 0x0002, lambda_1BD3)

    @scena.Lambda('lambda_1BE3')
    def lambda_1BE3():
        ChrTurnDirection(0x0101, 0x0103, 0)
        Yield()

        Jump('lambda_1BE3')

    DispatchAsync2(0x0101, 0x0000, lambda_1BE3)

    ChrWalkTo(0x0103, -30, 5100, -1630, 2000, 0x00)
    ChrSetDirection(0x0103, 14, 400)
    Sleep(500)

    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 59)
    PlaySE(6, 0x00, 0x64)
    OP_73(0x0000)
    ChrWalkTo(0x0103, -30, 5100, 270, 2000, 0x00)
    OP_6F(0x0000, 59)
    OP_70(0x0000, 0)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x0000)
    TerminateThread(0x0101, 0x00)
    OP_71(0x0000, 0x0800)
    FormationDelMember(0x02, 0xFF)

    def _loc_1C5F(): pass

    label('loc_1C5F')

    SetScenaFlags(ScenaFlag(0x0240, 5, 0x1205))
    Fade(1000)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1C6A
@scena.Code('func_07_1C6A')
def func_07_1C6A():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1CE7'),
        (0x00000001, 'loc_1CED'),
        (-1, 'loc_1CF3'),
    )

    def _loc_1CE7(): pass

    label('loc_1CE7')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1CF3')

    def _loc_1CED(): pass

    label('loc_1CED')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1CF3')

    def _loc_1CF3(): pass

    label('loc_1CF3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1D01',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1D05')

    def _loc_1D01(): pass

    label('loc_1D01')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1D05(): pass

    label('loc_1D05')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
