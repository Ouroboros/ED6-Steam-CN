import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T1211_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1211   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1211.x'
    header.mapIndex       = 1
    header.bgm            = 84
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT26/CH20365._CH', 'ED6_DT26/CH20365P._CP'),
        ('ED6_DT26/CH20351._CH', 'ED6_DT26/CH20351P._CP'),
        ('ED6_DT26/CH20350._CH', 'ED6_DT26/CH20350P._CP'),
        ('ED6_DT26/CH20366._CH', 'ED6_DT26/CH20366P._CP'),
        ('ED6_DT26/CH20206._CH', 'ED6_DT26/CH20206P._CP'),
        ('ED6_DT26/CH20205._CH', 'ED6_DT26/CH20205P._CP'),
        ('ED6_DT26/CH20425._CH', 'ED6_DT26/CH20425P._CP'),
        ('ED6_DT26/CH20455._CH', 'ED6_DT26/CH20455P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '锅',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '提妲',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x19A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x19A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x19A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x19A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1B9',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x53),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)
    Event(0, func_02_1DE)

    Jump('loc_1D5')

    def _loc_1B9(): pass

    label('loc_1B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_1D5',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x50),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)
    Event(0, func_03_1C97)

    def _loc_1D5(): pass

    label('loc_1D5')

    Return()

# id: 0x0001 offset: 0x1D6
@scena.Code('func_01_1D6')
def func_01_1D6():
    OP_B1('T1211')

    Return()

# id: 0x0002 offset: 0x1DE
@scena.Code('func_02_1DE')
def func_02_1DE():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    CameraMove(-25200, 0, 47910, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0008, -24200, 400, 47000, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetPos(0x0009, -28470, 0, 41130, 270)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x0009, 7)
    ChrSetSubChip(0x0009, 0)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 2)
    ChrSetSubChip(0x0008, 0)
    ChrSetFlags(0x0008, 0x0004)
    OP_6F(0x0000, 10)
    ChrSetPos(0x000B, -29470, 700, 41170, 0)
    ChrClearFlags(0x000B, 0x0080)
    LoadEffect(0x00, 'map\\\\onsen00.eff')
    OP_C5(0x00, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS106._CH')
    OP_C5(0x01, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS192._CH')
    OP_C5(0x02, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS193._CH')
    OP_C5(0x03, 0, 0, 640, 480, 0, 0, 768, 512, 0, 0, 640, 480, 0x00FFFFFF, 0x00, 'C_VIS194._CH')
    Sleep(1000)

    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('少女的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301619V……我说，哥哥…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301620V…………哥哥啊…………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Sleep(500)

    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, -1, 1500, 0)
    Sleep(2000)

    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('红发少女')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301621V嘿嘿，这次的生日，\n',
            '你可要期待着哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301622V我会送给哥哥你\n',
            '看了就会很高兴的礼物⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 300, -1, -1)
    TalkSetChrName('红发少年')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0050301623V是吗……\n',
            '我看了会高兴的东西啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301624V你是不是要做什么\n',
            '好吃的给我？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('红发少女')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301625V真是的～怎么想到吃上面去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301626V生日礼物当然应该是\n',
            '可以保存的有形的东西啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 300, -1, -1)
    TalkSetChrName('红发少年')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0050301627V那种东西吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301628V嗯～有形的、\n',
            '我看了又会高兴的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301629V是能用来打猎的小刀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('红发少女')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301630V你不是刚从村长\n',
            '那里拿到了小刀啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('红发少女')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301631V答案是我亲手做的\n',
            '首饰！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301632V虽然还没完成。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 300, -1, -1)
    TalkSetChrName('红发少年')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0050301633V你、你等等！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301634V我又不是女人，\n',
            '要首饰干吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('红发少女')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301635V哥哥已经～\n',
            '和时代脱节了啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301636V男孩子只要戴上一件\n',
            '装饰的首饰\n',
            '就会变得很酷的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301637V一定能让外表冷冰冰的\n',
            '哥哥变得有人气的哦⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 300, -1, -1)
    TalkSetChrName('红发少年')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0050301638V我说啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x02, 0x04, 0, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('红发少女')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301639V不可以……吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301640V我想对平时照顾\n',
            '我的哥哥表示感谢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301641V拼命在做着……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 300, -1, -1)
    TalkSetChrName('红发少年')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0050301642V唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301643V不、不是那种很可爱，很\n',
            '艳丽的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x04, 0, 0, 0)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('红发少女')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301644V嘿嘿，不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301645V简单又帅气的造型，\n',
            '十分适合哥哥的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301646V哥哥个子又高，\n',
            '肯定很合适的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 300, -1, -1)
    TalkSetChrName('红发少年')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0050301647V好～知道了知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301648V我会尽量期待的，\n',
            '加油做吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x01, 0x04, 0, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('红发少女')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301649V嘿嘿……嗯！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301650V我说，哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(50, 300, -1, -1)
    TalkSetChrName('阿加特')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0050301651V怎么了，米夏？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x03, 0x04, 0, 0, 0)
    OP_C6(0x03, 0x03, 16777215, 0, 0)
    OP_C6(0x03, 0x03, -1, 500, 0)
    Sleep(500)

    SetMessageWindowPos(320, 260, -1, -1)
    TalkSetChrName('米夏')

    Talk(
        (
            (TxtCtl.SetColor, 0xC),
            '#0710301652V一直以来，谢谢你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0710301653V总是保护着我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C6(0x00, 0x03, 16777215, 0, 0)
    OP_C6(0x01, 0x03, 16777215, 0, 0)
    OP_C6(0x02, 0x03, 16777215, 0, 0)
    OP_C6(0x03, 0x03, 16777215, 1000, 0)
    FadeOut(2000, 16777215, -1)
    OP_0D()
    OP_C7(0x00, 0x03, 0x03)
    OP_C6(0x00, 0x06, 0, 0, 0)
    OP_C6(0x01, 0x06, 0, 0, 0)
    OP_C6(0x02, 0x06, 0, 0, 0)
    OP_C6(0x03, 0x06, 0, 0, 0)
    Sleep(3000)

    PlayEffect(0x00, 0x00, 0x000B, 300, 400, -300, 0, 0, 0, 300, 200, 300, 0x00FF, 0, 0, 0, 0)
    FadeIn(2000, 16777215)
    OP_0D()
    Sleep(500)

    OP_99(0x0008, 0x0A, 0x0B, 1000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301654V#1281F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000258, 1400, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1500)

    OP_63(0x0008)
    OP_99(0x0008, 0x0B, 0x0A, 1000)
    Sleep(100)

    ChrSetSubChip(0x0008, 0)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301655V#1282F#5P是……梦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x0A, 0x0B, 1000)
    Sleep(100)

    ChrSetSubChip(0x0008, 15)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301656V#1289F#5P这里是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0009,
        '少女的声音',
        (
            '#0070301657V#2P……嗯，这样就行了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0009, 255, 255, 255, 255, 1000)
    OP_62(0x0008, 0x00000258, 1400, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrSetSubChip(0x0008, 11)
    Sleep(100)

    ChrSetSubChip(0x0008, 12)

    ChrTalk(
        0x0008,
        (
            '#0050301658V#1281F#2P米夏……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(-27180, 0, 44810, 2000)
    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '#0070301659V#1264F#5P阿加特哥哥！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301660V#1261F太好了……\n',
            '你醒了啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E64')
    def lambda_0E64():
        ChrWalkTo(0x00FE, -25480, 0, 46660, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0E64)

    @scena.Lambda('lambda_0E7F')
    def lambda_0E7F():
        CameraMove(-25360, 0, 48370, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_0E7F)

    WaitForThreadExit(0x0009, 0x0001)
    ChrSetDirection(0x0009, 90, 400)
    WaitForThreadExit(0x0009, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0050301661V#1281F#4P小鬼头……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301662V#1263F#5P那个那个，你身体\n',
            '不要紧了吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301663V#1280F#4P嗯，没什么──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 40)
    OP_99(0x0008, 0x00, 0x04, 900)
    OP_9E(0x0008, 20, 0, 300, 3000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301664V#1285F#4P痛……',
            TxtCtl.Enter,
        ),
    )

    OP_99(0x0008, 0x07, 0x09, 1200)
    CloseMessageWindow()
    OP_62(0x0009, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0009, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0009,
        (
            '#0070301665V#1265F#5P不、不行的～！\n',
            '你必须老老实实地躺着！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301666V伤口还没有\n',
            '完全愈合！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 40)
    OP_70(0x0000, 60)
    OP_99(0x0008, 0x09, 0x07, 1000)
    OP_99(0x0008, 0x04, 0x06, 1000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301667V#1280F#4P去，这点伤算不了\n',
            '什么的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301668V不管它自己也会好起来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 9)
    ChrSetSubChip(0x0009, 0)
    OP_99(0x0009, 0x00, 0x01, 2000)
    Sleep(250)

    ChrTalk(
        0x0009,
        (
            '#0070301669V#1268F#5P#3S不、不行！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    ChrSetSubChip(0x0009, 5)
    OP_0D()
    Sleep(250)

    OP_99(0x0009, 0x05, 0x03, 1500)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0070301670V#1262F#5P我和姐姐\n',
            '说好了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301671V在阿加特哥哥恢复之前\n',
            '绝对不让你下床！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x12, 0x14, 1200)
    Sleep(250)

    ChrTalk(
        0x0008,
        (
            '#0050301672V#1281F#4P喂、喂……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301673V#1262F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301674V#1284F#4P明白了，明白了啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x14, 0x12, 1000)
    Sleep(100)

    OP_6F(0x0000, 30)
    OP_70(0x0000, 10)
    OP_99(0x0008, 0x06, 0x00, 1000)
    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#0070301675V#1271F#5P……呼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 7)
    ChrSetSubChip(0x0009, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301676V#1282F#4P真是的……\n',
            '那么激动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x0A, 0x0B, 1200)
    OP_99(0x0008, 0x0B, 0x0C, 1200)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0050301677V#1281F#4P说起来，已经是晚上了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301678V艾丝蒂尔她们怎么样了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301679V#1260F#5P嗯，姐姐她们已经\n',
            '先回柏斯去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301680V好象她们有和将军的约定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301681V#1284F#4P和将军的约定？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲向阿加特传达了艾丝蒂尔的口信。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0008,
        (
            '#0050301682V#1280F#4P……是吗，\n',
            '说动了那个摩尔根啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301683V那么，军队也该\n',
            '联络协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 11)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301684V#1283F#4P好，那么我也快点……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301685V#1262F#5P…………………（盯。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301686V#1288F#4P……不过\n',
            '今天已经太晚了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301687V#1280F明早再回\n',
            '柏斯吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301688V#1265F#5P可、可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetSubChip(0x0008, 12)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0050301689V#1280F#4P睡得很充足，\n',
            '体力也恢复了很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301690V而且都是一些擦伤，\n',
            '这伤就算活动着也会自然好的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301691V没问题，不用担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301692V#1263F#5P你没……硬撑吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301693V#1293F#4P我说啊，我可是一名正游击士。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301694V我还没有莽撞到面对结社和龙\n',
            '都敢硬撑的程度啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301695V#1289F……而且也不能再让你\n',
            '继续遇险了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301696V#1264F#5P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301697V#1280F#4P反正我可没胆量\n',
            '得罪可怕的督察员小姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301698V就彻底相信我吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301699V#1271F#5P真、真是的……\n',
            '阿加特哥哥你这人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301700V#1260F不过看起来\n',
            '真的挺精神的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301701V#1280F#4P所以我就说嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301702V自己的身体自己\n',
            '最清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301703V#1266F#5P嘿嘿……太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301704V#1269F…………啊………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 4)
    ChrSetSubChip(0x0009, 0)
    OP_99(0x0009, 0x00, 0x06, 1000)
    OP_62(0x0008, 0x00000258, 1400, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0050301705V#1284F#4P怎、怎么了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301706V#1272F#5P呜……呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_B0(0x0000, 0x0A)
    OP_6F(0x0000, 10)
    OP_70(0x0000, 60)
    OP_99(0x0008, 0x00, 0x06, 1500)
    OP_99(0x0008, 0x12, 0x14, 1500)
    OP_62(0x0008, 0x00000000, 1600, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0050301707V#1284F#4P我、我都说了我\n',
            '已经没事了啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301708V我对女神发誓\n',
            '我没撒谎！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301709V#1272F#5P呜……\n',
            '……不、不是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301710V一放下心来……我就……\n',
            '不知道怎么的………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301711V#1269F呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x07, 0x0B, 1000)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070301712V#1268F#5P#4S呜哇啊啊啊啊啊啊……！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)

    @scena.Lambda('lambda_1A22')
    def lambda_1A22():
        OP_99(0x00FE, 0x0B, 0x0D, 1000)
        Yield()

        Jump('lambda_1A22')

    DispatchAsync2(0x0009, 0x0001, lambda_1A22)

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301713V#1288F#4P啊～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301714V#1290F真拿你没办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(800)
    ChrSetPos(0x0008, -25540, 0, 46100, 270)
    ChrClearFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    OP_B0(0x0000, 0x0F)
    OP_6F(0x0000, 20)
    OP_70(0x0000, 10)
    CameraMove(-26020, 0, 47720, 1000)
    OP_0D()
    ChrSetDirection(0x0008, 0, 400)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0008, 0x0002)
    TerminateThread(0x0009, 0x01)
    ChrSetSubChip(0x0009, 16)
    Sleep(1000)

    OP_99(0x0009, 0x11, 0x16, 1000)

    @scena.Lambda('lambda_1AF1')
    def lambda_1AF1():
        OP_99(0x00FE, 0x16, 0x12, 1000)
        Yield()

        Jump('lambda_1AF1')

    DispatchAsync2(0x0009, 0x0001, lambda_1AF1)

    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301715V#1290F#6P……对不起。\n',
            '让你那么担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301716V一个人昏了头的冲出去，\n',
            '还打了一场没有胜算的架……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301717V想不到最后\n',
            '还让你那么担心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301718V#1269F#2P……就是啊！\n',
            '阿加特哥哥是个傻瓜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0x01)
    OP_99(0x0009, 0x17, 0x1F, 1500)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070301719V#1272F#2P我……我……\n',
            '我真的很担心的啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301720V#1290F#6P嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301721V#1291F我真是……一个大傻瓜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 6, 0x10F6))
    NewScene('ED6_DT21/E0811._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x1C97
@scena.Code('func_03_1C97')
def func_03_1C97():
    EventBegin(0x00)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    CameraMove(-26550, 0, 42500, 0)
    OP_67(0, 5150, -10000, 0)
    CameraSetDistance(2850, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0008, -25540, 0, 46100, 0)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x000B, -29470, 700, 41170, 0)
    ChrClearFlags(0x000B, 0x0080)
    LoadEffect(0x00, 'map\\\\onsen00.eff')
    PlayEffect(0x00, 0x00, 0x000B, 300, 400, -300, 0, 0, 0, 300, 200, 300, 0x00FF, 0, 0, 0, 2000)
    ChrSetPos(0x0009, -25480, 0, 46660, 180)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetFlags(0x0009, 0x0040)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 4)
    ChrSetSubChip(0x0009, 31)
    OP_6F(0x0000, 5)

    @scena.Lambda('lambda_1D9B')
    def lambda_1D9B():
        CameraMove(-26020, 0, 47720, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D9B)

    @scena.Lambda('lambda_1DB3')
    def lambda_1DB3():
        OP_67(0, 6150, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1DB3)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    OP_DC()

    ChrTalk(
        0x0009,
        (
            '#0070301722V#1271F#2P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301723V#1290F#6P……好一点了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301724V#1271F#2P…………（擤鼻子）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x1F, 0x23, 800)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0070301725V#1263F#2P对、对不起。\n',
            '突然就哭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301726V#1288F#6P真是的，你可别\n',
            '吓我啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301727V真是的，比对付银发小子\n',
            '还要让人提心吊胆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301728V#1267F#2P嘿嘿……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301729V#1264F啊，对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x23, 0x21, 800)
    Sleep(300)

    ChrTalk(
        0x0009,
        (
            '#0070301730V#1260F#2P那个那个，阿加特哥哥。\n',
            '肚子饿了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301731V我从村长那儿拿了材料\n',
            '做了热汤……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301732V#1280F#6P喔，怪不得\n',
            '有一股香味呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301733V#1281F……咦，等等。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301734V怎么会有厨房……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301735V#1264F#2P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 7)
    ChrSetSubChip(0x0009, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 6)
    ChrSetSubChip(0x0008, 0)
    OP_0D()

    @scena.Lambda('lambda_208D')
    def lambda_208D():
        CameraMove(-27810, 0, 45350, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_208D)

    ChrSetDirection(0x0008, 270, 400)
    ChrSetDirection(0x0008, 180, 400)
    Sleep(1000)

    ChrWalkTo(0x0008, -25930, 0, 44430, 1000, 0x00)
    Sleep(500)

    ChrSetDirection(0x0008, 90, 400)
    Sleep(500)

    ChrSetDirection(0x0008, 270, 400)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0050301736V#1284F#6P仔细看看……还真让人吃惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301737V虽然有点些微的差别，\n',
            '不过几乎和那时候一模一样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_215D')
    def lambda_215D():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_215D')

    DispatchAsync2(0x0009, 0x0001, lambda_215D)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_218A')
    def lambda_218A():
        CameraMove(-26430, 0, 47750, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_218A)

    ChrSetDirection(0x0008, 0, 400)
    Sleep(1000)

    ChrWalkTo(0x0008, -26310, 0, 46940, 1000, 0x00)
    WaitForThreadExit(0x0000, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301738V#1290F#3P再加上还有这个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301739V#1291F呵……\n',
            '想不到这东西还会留存下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301740V#1264F#4P？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301741V#1290F#5P噢，你不明白是吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301742V……其实这个家，\n',
            '在十年前被完全烧毁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301743V#1270F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301744V#1282F#5P帝国军的燃烧弹\n',
            '变成流弹射进村里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301745V一转眼这个屋子都着了火，\n',
            '瞬间烧成黑炭了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301746V#1289F我知道后来村长\n',
            '又好心地重建了起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301747V不过没想到连\n',
            '屋内的布置都和过去一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301748V#1265F#4P…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301749V#1280F#5P虽然我从来没\n',
            '进过这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301750V不过他们竟能做到这个地步，\n',
            '还真得去道个谢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301751V#1265F#4P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301752V……那……那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301753V那时……米夏姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301754V#1282F#5P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301755V#1290F……哈哈，被你看穿了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0008, 90, 300)

    @scena.Lambda('lambda_2548')
    def lambda_2548():
        CameraMove(-26720, 0, 47740, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2548)

    ChrMoveTo(0x0008, -26650, 0, 46760, 500, 0x00)
    TerminateThread(0x0009, 0x01)
    Fade(1000)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 3)
    ChrSetSubChip(0x0008, 0)
    ChrSetPos(0x0008, -26500, 0, 46620, 90)
    OP_0D()
    Sleep(500)

    OP_99(0x0008, 0x00, 0x02, 800)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301756V#1282F#5P……她为我准备了\n',
            '生日礼物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301757V亲手做的……\n',
            '一件十分适合我的首饰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301758V在去山道避难的途中，那家伙\n',
            '回家去取那个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301759V然后燃烧弹就掉落了下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301760V#1263F#4P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301761V#1289F#5P她在被救出来的时候……\n',
            '已经全身严重烧伤了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301762V尽管如此，她仍然紧握\n',
            '着那件首饰……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301763V金属部分虽然不行了，\n',
            '不过石头的部分还安然无恙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301764V#1290F就是这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x02, 0x04, 800)
    Sleep(300)

    OP_99(0x0008, 0x04, 0x07, 800)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0070301765V#1270F#4P……啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301766V#1290F#5P既不是七耀石也不是什么宝石，\n',
            '只是一颗漂亮的石头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301767V大概是在这附近的\n',
            '小河里找到的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301768V#1282F我怎么也想不通\n',
            '她为什么要为了这样的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301769V不过奇怪的是\n',
            '我一点都不生她的气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x07, 0x09, 800)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301770V#1289F#5P虽然我没什么留做纪念的意思……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301771V不过当战争结束我离开了村庄，\n',
            '在外过着颓废的生活时，\n',
            '也只有这件东西是我无法割舍的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301772V#1290F哈哈……很丢人吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301773V#1262F#4P没、没有……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301774V#1282F#5P真的是很丢人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301775V看着这东西时，\n',
            '我就能忘记愤怒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301776V#1286F对没出息的我没能\n',
            '救出米夏的那种愤怒……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301777V#1265F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301778V#1289F#5P通过把这种骚动的怒火\n',
            '灌注在重剑上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301779V总算我还没有\n',
            '迷失自我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301780V#1291F……在自我欺骗中\n',
            '无法前进的废物……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301781V呵呵呵……\n',
            '那个家伙没说错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301782V#1263F#4P阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301783V#1280F#5P不……应该更加差劲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301784V一个只知道闭目不看那些不想看的东西，\n',
            '一味逃跑的白痴小子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301785V是我最讨厌的丧家之犬。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301786V#1292F#5P#3S哈哈哈，这真是好笑！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301787V#1263F#4P阿加特……哥哥……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301788V#1271F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000007D0)

    @scena.Lambda('lambda_2C82')
    def lambda_2C82():
        CameraMove(-26900, 0, 47740, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2C82)

    ChrWalkTo(0x0009, -25950, 0, 46660, 500, 0x00)
    ChrSetPos(0x0009, -26480, 0, 46610, 270)
    ChrSetPos(0x000C, -25950, 0, 46610, 270)
    ChrSetFlags(0x0009, 0x8000)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 3)
    ChrSetSubChip(0x0009, 48)
    OP_99(0x0009, 0x30, 0x32, 1000)
    PlayBGM(118)
    Sleep(500)

    ChrTalk(
        0x000C,
        (
            '#0070301789V#1271F#4P我……\n',
            '虽然不能完全理解\n',
            '阿加特哥哥的心情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301790V也不知道\n',
            '你为什么痛苦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301791V#1262F可是，有一句话我想\n',
            '代替米夏姐姐说给你听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x0A, 0x0B, 1000)

    ChrTalk(
        0x0008,
        (
            '#0050301792V#1281F#5P……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)

    @scena.Lambda('lambda_2DCE')
    def lambda_2DCE():
        CameraSetDistance(2700, 500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_2DCE)

    OP_0D()

    ChrTalk(
        0x000C,
        (
            '#0070301793V#1268F#4P#3S……不要把我很喜欢\n',
            '的哥哥看扁！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(
        0x000C,
        (
            '#0070301794V#1274F#4P你根本不了解我哥哥\n',
            '身上的优点！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301795V我最了解\n',
            '哥哥了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301796V#1268F我不允许任何人\n',
            '把他说得那么坏，\n',
            '即便是他本人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0xFFFFFF6A, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301797V#1284F#5P什……么…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2F09')
    def lambda_2F09():
        CameraMove(-27000, 0, 47520, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2F09)

    OP_99(0x0009, 0x33, 0x37, 1200)

    @scena.Lambda('lambda_2F2A')
    def lambda_2F2A():
        OP_99(0x0009, 0x38, 0x3B, 1200)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_2F2A)

    @scena.Lambda('lambda_2F3A')
    def lambda_2F3A():
        OP_99(0x0008, 0x18, 0x1B, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2F3A)

    WaitForThreadExit(0x0000, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301798V#1281F#5P………啊…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301799V#1272F#4P虽然我可能不及\n',
            '米夏姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301800V即便如此，我仍然知道很多\n',
            '阿加特哥哥身上的优点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301801V所以，听到你把自己说得那么坏\n',
            '我感到很悲伤……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301802V阿加特哥哥\n',
            '根本不了解自己，\n',
            '想到这一点我就很生气……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301803V所以……所以……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301804V#1281F#5P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301805V#1291F……哈哈……败给你了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301806V#1290F用和米夏一样的口气\n',
            '把我教训了一番……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301807V明明是个小鬼，\n',
            '想不到这么聪明……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301808V#1274F#4P请、请别把我\n',
            '当小孩子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301809V我……我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070301810V#1272F真的很悲伤……\n',
            '所以也很生气……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301811V#1290F#5P……是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301812V#1291F…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301813V我根本不了解\n',
            '我自己吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301814V……好象说的没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)

    @scena.Lambda('lambda_327D')
    def lambda_327D():
        CameraMove(-26720, 0, 47740, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_327D)

    ChrClearFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 7)
    ChrSetSubChip(0x0009, 0)
    ChrSetSubChip(0x0008, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetFlags(0x0009, 0x0020)
    ChrSetPos(0x0008, -26640, 0, 46620, 90)
    ChrSetPos(0x0009, -26070, 0, 46640, 270)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetChipByIndex(0x0008, 5)
    ChrSetSubChip(0x0008, 0)
    OP_0D()
    Sleep(500)

    OP_99(0x0008, 0x00, 0x04, 800)
    OP_99(0x0008, 0x04, 0x02, 800)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0070301815V#1273F#4P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0050301816V#1290F#5P谢谢你，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301817V你提醒得对。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070301818V#1266F#4P阿加特哥哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x05, 0x06, 800)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301819V#1282F#5P……用自己的尺度\n',
            '来衡量自己是不行的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301820V那么我就努力挣扎一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301821V有愤怒和悲哀都没关系……\n',
            '在找到答案之前，要一直前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x06, 0x0B, 900)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0050301822V#1290F#5P嘿嘿，这样的话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050301823V一直带着这东西的\n',
            '意义也总有一天会浮现出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_DB()
    FadeOut(3000, 0, -1)
    OP_0D()
    OP_20(0x00000BB8)
    OP_21()
    Sleep(500)

    PlaySE(13, 0x00, 0x64)
    Sleep(2000)

    Sleep(2000)

    Sleep(1500)

    OP_DC()
    MapClearFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T1103._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x34F3
@scena.Code('func_04_34F3')
def func_04_34F3():
    ChrWalkTo(0x00FE, -25950, 0, 46660, 1000, 0x00)
    ChrSetPos(0x0009, -26500, 0, 46620, 270)
    ChrSetFlags(0x0009, 0x8000)
    ChrSetFlags(0x0009, 0x0002)
    ChrSetChipByIndex(0x0009, 3)
    ChrSetSubChip(0x0009, 32)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
