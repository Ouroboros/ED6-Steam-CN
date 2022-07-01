import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4222_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4222   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '里拉老人'),
    TXT(0x02, '艾科尔'),
    TXT(0x03, '希尔丹夫人'),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4222.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x276E
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
        ('ED6_DT06/CH20008._CH', 'ED6_DT06/CH20008P._CP'),
        ('ED6_DT06/CH20107._CH', 'ED6_DT06/CH20107P._CP'),
        ('ED6_DT07/CH00127._CH', 'ED6_DT07/CH00127P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01350._CH', 'ED6_DT07/CH01350P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -138710,
            z                   = 0,
            y                   = 7150,
            direction           = 6,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = -74270,
            z                   = 0,
            y                   = 1530,
            direction           = 6,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
    )

# id: 0x10003 offset: 0x13A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x13A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x13A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x13A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_14B',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)

    def _loc_14B(): pass

    label('loc_14B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 6, 0x1626)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16D',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -144740, 0, 7150, 0)

    def _loc_16D(): pass

    label('loc_16D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_17A',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_17A(): pass

    label('loc_17A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 2, 0x1002)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_186',
    )

    Event(0, 0x0007)

    def _loc_186(): pass

    label('loc_186')

    Return()

# id: 0x0001 offset: 0x187
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1A3',
    )

    OP_B1('t4222_y')

    Jump('loc_1AC')

    def _loc_1A3(): pass

    label('loc_1A3')

    OP_B1('t4222_n')

    def _loc_1AC(): pass

    label('loc_1AC')

    Return()

# id: 0x0002 offset: 0x1AD
@scena.Code('ReInit')
def ReInit():
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
        'loc_1D2',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_314')

    def _loc_1D2(): pass

    label('loc_1D2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1EB',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    Jump('loc_314')

    def _loc_1EB(): pass

    label('loc_1EB')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_204',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x0000060E)

    Jump('loc_314')

    def _loc_204(): pass

    label('loc_204')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21D',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005DC)

    Jump('loc_314')

    def _loc_21D(): pass

    label('loc_21D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_236',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AA)

    Jump('loc_314')

    def _loc_236(): pass

    label('loc_236')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24F',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x00000578)

    Jump('loc_314')

    def _loc_24F(): pass

    label('loc_24F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_268',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x00000546)

    Jump('loc_314')

    def _loc_268(): pass

    label('loc_268')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_281',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000677)

    Jump('loc_314')

    def _loc_281(): pass

    label('loc_281')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29A',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000645)

    Jump('loc_314')

    def _loc_29A(): pass

    label('loc_29A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B3',
    )

    OP_99(0x00FE, 0x02, 0x07, 0x00000613)

    Jump('loc_314')

    def _loc_2B3(): pass

    label('loc_2B3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CC',
    )

    OP_99(0x00FE, 0x03, 0x07, 0x000005E1)

    Jump('loc_314')

    def _loc_2CC(): pass

    label('loc_2CC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E5',
    )

    OP_99(0x00FE, 0x04, 0x07, 0x000005AF)

    Jump('loc_314')

    def _loc_2E5(): pass

    label('loc_2E5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2FE',
    )

    OP_99(0x00FE, 0x05, 0x07, 0x0000057D)

    Jump('loc_314')

    def _loc_2FE(): pass

    label('loc_2FE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_314',
    )

    OP_99(0x00FE, 0x06, 0x07, 0x0000054B)

    def _loc_314(): pass

    label('loc_314')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_329',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_314')

    def _loc_329(): pass

    label('loc_329')

    Return()

# id: 0x0003 offset: 0x32A
@scena.Code('func_03_32A')
def func_03_32A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_34D',
    )

    OP_8D(0x00FE, -75980, 4000, -69120, -620, 2000)

    Jump('func_03_32A')

    def _loc_34D(): pass

    label('loc_34D')

    Return()

# id: 0x0004 offset: 0x34E
@scena.Code('func_04_34E')
def func_04_34E():
    TalkBegin(0x000A)
    Call(0, 0x0008)
    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x359
@scena.Code('func_05_359')
def func_05_359():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_3C2',
    )

    ChrTalk(
        0x00FE,
        (
            '在太阳下山之前\n',
            '必须要做完全部的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在没有导力器的现在，\n',
            '天一黑就伸手不见五指。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D1')

    def _loc_3C2(): pass

    label('loc_3C2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_444',
    )

    ChrTalk(
        0x00FE,
        (
            '情报部的余党都被捕了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁让他们搞得王国不得安宁，\n',
            '真是自作自受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一定要让他们和理查德上校\n',
            '一同赎罪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4D1')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_4D1',
    )

    ChrTalk(
        0x00FE,
        (
            '《王城设计图》、《七至宝》、\n',
            '《百日战役全貌》……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '陛下命令我整理出\n',
            '被情报部带走的书的清单。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '陛下到底是想调查什么呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4D1(): pass

    label('loc_4D1')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x4D5
@scena.Code('func_06_4D5')
def func_06_4D5():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_52C',
    )

    ChrTalk(
        0x00FE,
        (
            '杜南公爵\n',
            '简直像变了个人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近甚至还在政务室\n',
            '接待来投诉的市民。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61E')

    def _loc_52C(): pass

    label('loc_52C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_5CF',
    )

    ChrTalk(
        0x00FE,
        (
            '听说在昨天的事件中杜南公爵\n',
            '被胁持为人质了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '谁让他这么晚还出去晃悠，\n',
            '真是自讨苦吃。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '明明被要求在离宫谨慎而居，\n',
            '可一点都没有在反省的样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_61E')

    def _loc_5CF(): pass

    label('loc_5CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_61E',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，赶紧\n',
            '打扫完客厅吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '客厅打扫完\n',
            '还要去里面的资料室帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_61E(): pass

    label('loc_61E')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x622
@scena.Code('func_07_622')
def func_07_622():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    SetMapFlags(0x00000080)
    SetChrPos(0x0103, -79000, 0, 9200, 180)
    SetChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 0)
    SetChrSubChip(0x0101, 0)
    SetChrFlags(0x0101, 0x0004)
    SetChrPos(0x0101, -29660, 350, 60680, 177)
    OP_69(0x0101, 0x00000000)

    ChrTalk(
        0x0101,
        (
            '#007F……唔～……好刺眼…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 16)
    Sleep(200)

    SetChrSubChip(0x0101, 0)
    Sleep(200)

    SetChrSubChip(0x0101, 16)
    Sleep(200)

    SetChrSubChip(0x0101, 0)
    OP_99(0x0101, 0x00, 0x08, 0x000003E8)
    Sleep(1500)

    @scena.Lambda('lambda_06C7')
    def lambda_06C7():
        OP_99(0x00FE, 0x08, 0x0C, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_06C7)

    ChrTalk(
        0x0101,
        (
            '#007F嘿～～～～～……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0101, 0x0000000F, 0x00000000, 0x000007D0, 0x00000FA0)

    @scena.Lambda('lambda_0705')
    def lambda_0705():
        OP_99(0x00FE, 0x0C, 0x0E, 0x000003E8)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0705)

    Sleep(1000)

    SetChrSubChip(0x0101, 14)
    Sleep(200)

    SetChrSubChip(0x0101, 17)
    Sleep(200)

    SetChrSubChip(0x0101, 18)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#007F嗯～～睡得挺好～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x0101, 18)
    Sleep(500)

    SetChrSubChip(0x0101, 20)
    Sleep(500)

    SetChrSubChip(0x0101, 18)
    Sleep(500)

    SetChrSubChip(0x0101, 20)
    Sleep(500)

    SetChrSubChip(0x0101, 18)
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010190004V#004F咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190005V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F对了，我们\n',
            '昨天留宿在王都里面了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#505F和约修亚一起逛了庆典……\n',
            '回来途中吃了冰淇淋……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190008V晚上和老爸一起参加晚餐会……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190009V……然后………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    OP_AD(0x00240027, 0x0000, 0x0000, 0x00000096)
    Sleep(3000)

    OP_AE(0x000000C8)
    Sleep(1000)

    OP_AD(0x00240028, 0x0000, 0x0000, 0x00000096)
    Sleep(3000)

    OP_AE(0x000000C8)
    Sleep(1000)

    OP_AD(0x00240029, 0x0000, 0x0000, 0x00000096)
    Sleep(3000)

    OP_AE(0x000000C8)
    Sleep(1000)

    OP_AD(0x0024002A, 0x0000, 0x0000, 0x00000096)
    Sleep(3000)

    OP_AE(0x000000C8)
    Sleep(1000)

    FadeIn(1500, 0)
    OP_0D()
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190010V#580F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190011V……不………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    Fade(500)
    OP_6B(3000, 0)
    ClearChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrPos(0x0101, -31510, 0, 60590, 176)
    OP_6A(0x0101)
    OP_0D()
    OP_8C(0x0101, 90, 1000)
    Sleep(1000)

    OP_8C(0x0101, 270, 1000)
    Sleep(1000)

    OP_8C(0x0101, 180, 1000)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#004F这是……\n',
            '约修亚和老爸的房间……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#505F我应该……\n',
            '是和雪拉姐睡一个房间的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190014V那个……\n',
            '……我是什么时候开始做梦的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    SetChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 1)
    SetChrSubChip(0x0101, 5)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010190015V#580F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010451292V………………………………\n',
            '………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#005F约修亚！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0101, 0x0002)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    Sleep(500)

    OP_8E(0x0101, -35090, 0, 48800, 7000, 0x00)
    ClearMapFlags(0x00000001)
    Fade(1000)
    OP_6D(-67000, 0, 7200, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, -67000, 0, 7200, 180)
    SetChrPos(0x0103, -79000, 0, 9200, 180)
    OP_0D()
    OP_8E(0x0101, -66780, 0, 3290, 5000, 0x00)
    OP_8C(0x0101, 90, 1000)
    Sleep(1000)

    OP_8C(0x0101, 270, 1000)
    Sleep(1000)

    OP_8C(0x0101, 90, 1000)
    OP_69(0x0103, 0x000007D0)
    OP_72(0x0003, 0x0010)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 0x0000003C)
    OP_73(0x0003)

    @scena.Lambda('lambda_0BC2')
    def lambda_0BC2():
        OP_69(0x0103, 0x00000000)
        Yield()

        Jump('lambda_0BC2')

    DispatchAsync2(0x0103, 0x0003, lambda_0BC2)

    OP_8E(0x0103, -78370, 0, 3070, 2000, 0x00)
    ChrTurnDirection(0x0103, 0x0101, 1000)
    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_8E(0x0103, -71160, 0, 2270, 2000, 0x00)
    TerminateThread(0x0103, 0x03)

    ChrTalk(
        0x0103,
        (
            '#021F哎呀，艾丝蒂尔。\n',
            '你可睡醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 1000)

    ChrTalk(
        0x0101,
        (
            '#003F雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#025F真是的，昨天那么晚还不回来，\n',
            '叫人担心死了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#021F不过看起来，你应该是\n',
            '和约修亚聊了很多──',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0103, 0x000007D0, 0x00001388, 0x00)

    ChrTalk(
        0x0101,
        (
            '#005F雪拉姐，约修亚在哪儿！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#005F我在找约修亚！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190025V雪拉姐，你见过他么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#023F今早是没见到……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#020F搞什么啊，你不是昨天太累了\n',
            '就睡在那边的房间了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030190028V醒来的时候他不在？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#580F咦……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我太累，就睡了……\n',
            '#005F你、你是听谁说的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F老师说的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#580F老、老爸！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010190033V#005F那么！\n',
            '你有没有看见老爸！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#020F老师他刚才走上楼梯\n',
            '去了空中庭园啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E99')
    def lambda_0E99():
        OP_8E(0x00FE, -56330, 0, 1420, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0E99)

    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#024F啊，等等，艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0103,
        (
            '#024F……怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    SetChrChipByIndex(0x0103, 2)
    OP_99(0x0103, 0x00, 0x0D, 0x000007D0)
    Sleep(1000)

    SetChrSubChip(0x0103, 0)
    SetChrChipByIndex(0x0103, 65535)

    ChrTalk(
        0x0103,
        (
            '#0030190038V#022F………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#026F逆位的『恋人』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1002)
    FadeOut(1000, 0, -1)
    OP_0D()
    FormationDelMember(0x02, 0xFF)
    NewScene('ED6_DT21/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0xF7B
@scena.Code('func_08_F7B')
def func_08_F7B():
    EventBegin(0x00)
    Fade(1000)
    SetChrPos(0x0105, -144700, 0, 5700, 360)
    SetChrPos(0x0101, -145560, 0, 5680, 360)
    SetChrPos(0x0104, -145320, 0, 4460, 360)
    SetChrPos(0x0108, -144920, 0, 3690, 360)
    OP_8C(0x000A, 180, 0)
    SetChrSubChip(0x000A, 0)
    OP_6D(-144440, 0, 6730, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0650251132V#712F#5P科洛蒂娅殿下！？\n',
            '还有艾丝蒂尔小姐也……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251133V#542F#4P希尔丹夫人。\n',
            '我回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251134V#1006F#6P那个，好久不见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251135V#711F#5P嗯，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251136V公主殿下在帮助\n',
            '艾丝蒂尔的事儿\n',
            '我也知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251137V你们两个……\n',
            '能平安回来真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251138V#1025F#6P希尔丹夫人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251139V#041F#4P呵呵，谢谢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251140V#040F其实我这次回来，\n',
            '也同时是为了协会的调查。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251141V有些事想问问\n',
            '希尔丹夫人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251142V#713F#5P请您随便问吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251143V#711F可是，这里似乎\n',
            '有点不太方便。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251144V我们去会客室吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    SetChrPos(0x000A, -34220, 0, -53190, 270)
    SetChrPos(0x0101, -35670, 0, -52660, 90)
    SetChrPos(0x0105, -35990, 0, -53890, 90)
    SetChrPos(0x0108, -37150, 0, -53340, 90)
    SetChrPos(0x0104, -35720, 0, -54910, 45)
    OP_6D(-34480, 0, -52400, 0)
    OP_67(0, 5520, -10000, 0)
    OP_6B(2960, 0)
    OP_6C(45000, 0)
    OP_6E(255, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0650251145V#712F#2P原来如此……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251146V你们在调查\n',
            '那封恐吓信啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251147V#710F那么你们想问我的是\n',
            '对罪犯的身份有没有线索？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251148V#1002F#6P是的，一点不错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251149V总之我们先要遍访\n',
            '各个收到恐吓信的地方……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251150V#713F#2P还真是辛苦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251151V#715F不过我这儿还真\n',
            '没有什么线索。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251152V我只能说我敢断言\n',
            '绝不是城堡里的人干的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251153V#1007F#6P唔～也是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251154V#042F寄到城堡里的恐吓信\n',
            '寄给谁收的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251155V#714F#2P是女王陛下，\n',
            '真让人心惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251156V因为寄给陛下的\n',
            '可疑信件都要接受检查，\n',
            '所以内容我也知道。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251157V#716F还真有这种胆大包天的\n',
            '不法之徒啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251158V#070F#6P我想冒昧问一下……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251159V还有没有什么其他的可疑信件\n',
            '被寄到城堡里？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251160V比如充满了对王室的\n',
            '批判的内容的文字之类的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251161V#712F#2P这……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251162V#043F希尔丹夫人。\n',
            '我也请求您说出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251163V我们需要尽可能多的\n',
            '判断材料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251164V#713F#2P您既然都这么说了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251165V#710F我们确实收到过\n',
            '好几封匿名信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251166V不过内容并非\n',
            '批评王室。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251167V多为请求给\n',
            '理查德上校减刑的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251168V我想这恐怕是来自\n',
            '一部分王都的市民……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251169V#1004F#6P这、这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251170V#035F呵呵，不愧是\n',
            '我过去的竞争对手。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251171V即便被捕，也还是受欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251172V#542F因为所有人都认可上校\n',
            '是位有能力的人物……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251173V有人替他惋惜\n',
            '也是人之常情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251174V#072F#6P不过此类信件看来\n',
            '和恐吓信没什么关系。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251175V#074F看来恐吓信的目的多半是\n',
            '企图动摇王室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251176V#1015F#6P唔～能了解到这一点\n',
            '也不错了',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251177V#1004F对了，希尔丹夫人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251178V还有一件事情\n',
            '想问您……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '询问了希尔丹夫人关于玲的双亲的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x000A,
        (
            '#0650251179V#712F#2P克洛斯贝尔贸易商，\n',
            '哈罗德·海瓦斯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251180V嗯，我知道。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0108, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0105, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    OP_62(0x0104, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010251181V#1005F#6P#3S啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251182V#044F是希尔丹夫人的\n',
            '相识吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251183V#710F#2P不，只不过他们前几天\n',
            '申请过城堡内的参观。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251184V因为我正好有空，\n',
            '就给他们带了路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251185V我记得他们夫妇\n',
            '还带着一个女儿吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251186V#1008F#6P是、是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251187V#035F不过这对找寻他们\n',
            '似乎构不成什么线索。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251188V#713F#2P可是……有件事让我比较在意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251189V#044F在意的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251190V#714F#2P他们的女儿虽然参观得\n',
            '很有兴致……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251191V不过相比之下，\n',
            '她的父母感觉心不在焉的样子。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251192V虽然和我说话时没什么异样，\n',
            '可我觉得那恐怕是勉强装出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251193V#074F#6P第一次来这里参观\n',
            '竟然心不在焉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251194V#072F很可能是有什么烦恼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251195V#043F嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251196V有可能那时候已经\n',
            '被卷进什么纠纷中去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251197V#030F嗯，说不定可以从\n',
            '这条线查下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251198V#1006F#6P希尔丹夫人，谢谢您。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251199V您给了我们\n',
            '很好的提示。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251200V#711F#2P那就太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251201V对了，公主殿下，还有各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251202V今晚你们应该会住在\n',
            '格兰赛尔城堡吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010200137V#1004F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251204V#040F我在王都的这段时间\n',
            '是准备住在这里的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251205V大家呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FDC',
    )

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
            TXT(0x00, '【◇已经和帝国大使对话】\n'),
            TXT(0x01, '【◇尚未和帝国大使对话】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1FBB'),
        (0x00000001, 'loc_1FD3'),
        (-1, 'loc_1FDC'),
    )

    def _loc_1FBB(): pass

    label('loc_1FBB')

    OP_A2(0x161B)
    OP_A2(0x161C)
    OP_A2(0x161D)
    OP_A2(0x161F)
    OP_A2(0x1620)
    OP_A2(0x1621)
    OP_A2(0x1622)

    Jump('loc_1FDC')

    def _loc_1FD3(): pass

    label('loc_1FD3')

    OP_A3(0x1621)
    OP_A3(0x1622)

    Jump('loc_1FDC')

    def _loc_1FDC(): pass

    label('loc_1FDC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            Expr.Return,
        ),
        'loc_20A8',
    )

    ChrTalk(
        0x0104,
        (
            '#0040251206V#031F我前面也说过了，\n',
            '我准备住在\n',
            '埃雷波尼亚大使馆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251207V所以这份好意我就心领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251208V#070F#6P我也准备留宿在\n',
            '卡尔瓦德大使馆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251209V就不劳烦各位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2162')

    def _loc_20A8(): pass

    label('loc_20A8')

    ChrTalk(
        0x0104,
        (
            '#0040251210V#031F啊，我今晚\n',
            '准备住在埃雷波尼亚\n',
            '大使馆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040251207V所以这份好意我就心领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251208V#070F#6P我也准备留宿在\n',
            '卡尔瓦德大使馆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080251209V就不劳烦各位了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2162(): pass

    label('loc_2162')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_220E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_220E',
    )

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
            TXT(0x00, '【◇在第１章选了阿加特作为同伴】\n'),
            TXT(0x01, '【◇在第１章选了雪拉扎德作为同伴】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2202'),
        (0x00000001, 'loc_2208'),
        (-1, 'loc_220E'),
    )

    def _loc_2202(): pass

    label('loc_2202')

    OP_A2(0x1201)

    Jump('loc_220E')

    def _loc_2208(): pass

    label('loc_2208')

    OP_A3(0x1200)

    Jump('loc_220E')

    def _loc_220E(): pass

    label('loc_220E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_226E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010251214V#1025F#1P唔～我得问问阿加特\n',
            '和提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251215V再说还有小玲在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_22C4')

    def _loc_226E(): pass

    label('loc_226E')

    ChrTalk(
        0x0101,
        (
            '#0010251216V#1025F#1P唔～我得问问雪拉姐\n',
            '和提妲……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251215V再说还有小玲在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_22C4(): pass

    label('loc_22C4')

    ChrTalk(
        0x0105,
        (
            '#0060251218V#542F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251219V#713F#2P那么我去准备一下房间，\n',
            '你们随时都可以\n',
            '过来住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251220V#1017F#6P谢谢您，希尔丹夫人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251221V#048F那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0650251222V#711F#2P请交给我吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251223V我先回女佣室了，\n',
            '各位\n',
            '请随意。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0650251224V那么，告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x000A, 0, 400)

    @scena.Lambda('lambda_23F6')
    def lambda_23F6():
        OP_6D(-34470, 0, -49910, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_23F6)

    @scena.Lambda('lambda_240E')
    def lambda_240E():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_240E')

    DispatchAsync2(0x0101, 0x0002, lambda_240E)

    @scena.Lambda('lambda_241F')
    def lambda_241F():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_241F')

    DispatchAsync2(0x0105, 0x0002, lambda_241F)

    @scena.Lambda('lambda_2430')
    def lambda_2430():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_2430')

    DispatchAsync2(0x0104, 0x0002, lambda_2430)

    @scena.Lambda('lambda_2441')
    def lambda_2441():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_2441')

    DispatchAsync2(0x0108, 0x0002, lambda_2441)

    OP_8E(0x000A, -35000, 0, -50800, 2000, 0x00)
    Sleep(200)

    OP_22(0x0006, 0x00, 0x64)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 0x0000003C)
    OP_73(0x0000)
    OP_8E(0x000A, -35060, 0, -48810, 2000, 0x00)
    TerminateThread(0x0101, 0x02)
    TerminateThread(0x0105, 0x02)
    TerminateThread(0x0104, 0x02)
    TerminateThread(0x0108, 0x02)
    SetChrFlags(0x000A, 0x0080)
    OP_72(0x0000, 0x0800)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)
    OP_23(0x0006)
    OP_22(0x0007, 0x00, 0x64)
    Sleep(500)

    OP_71(0x0000, 0x0800)
    OP_6D(-35580, 0, -52640, 1600)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2574',
    )

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
            TXT(0x00, '【◇已经和女王对话】\n'),
            TXT(0x01, '【◇尚未和女王对话】\n'),
            TXT(0x02, '【◇什么也没有变更】\n'),
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
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2568'),
        (0x00000001, 'loc_256E'),
        (-1, 'loc_2574'),
    )

    def _loc_2568(): pass

    label('loc_2568')

    OP_A2(0x1625)

    Jump('loc_2574')

    def _loc_256E(): pass

    label('loc_256E')

    OP_A3(0x1625)

    Jump('loc_2574')

    def _loc_2574(): pass

    label('loc_2574')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2652',
    )

    OP_8C(0x0101, 225, 400)

    @scena.Lambda('lambda_2589')
    def lambda_2589():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2589)

    OP_8C(0x0104, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251225V#1006F#5P好了……\n',
            '接下来得去见女王陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251226V她应该在女王宫吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060251227V#040F嗯，我想是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040251228V#035F哼哼，那么\n',
            '去向她老人家打招呼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2736')

    def _loc_2652(): pass

    label('loc_2652')

    OP_8C(0x0101, 225, 400)

    @scena.Lambda('lambda_265F')
    def lambda_265F():
        OP_8C(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_265F)

    OP_8C(0x0104, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251229V#1006F#5P好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251230V这样一来从女王陛下和\n',
            '希尔丹夫人那里都打听过情况了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080251231V#070F#6P我们也该出城堡\n',
            '回市区了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010251232V#1011F#5P嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x008B, 0x02, 0x0080)
    OP_28(0x008B, 0x01, 0x0100)

    def _loc_2736(): pass

    label('loc_2736')

    Sleep(100)

    OP_A2(0x1626)
    OP_28(0x008B, 0x01, 0x0800)
    OP_28(0x008A, 0x01, 0x0004)
    OP_28(0x008A, 0x01, 0x0008)

    ExecExpressionWithVar(
        0x31,
        (
            (Expr.PushLong, 0xC7),
            Expr.Nop,
            Expr.Return,
        ),
    )

    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
