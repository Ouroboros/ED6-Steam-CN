import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3116_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3116   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拉赛尔博士'),
    TXT(0x02, '提妲'),
    TXT(0x03, '玛多克工房长'),
    TXT(0x04, '加鲁诺'),
    TXT(0x05, '普罗梅笛'),
    TXT(0x06, '安东尼'),
    TXT(0x07, '导力器'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3116.x'
    header.mapIndex       = 1
    header.bgm            = 13
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x457E
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
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH02620._CH', 'ED6_DT07/CH02620P._CP'),
        ('ED6_DT07/CH01190._CH', 'ED6_DT07/CH01190P._CP'),
        ('ED6_DT07/CH01100._CH', 'ED6_DT07/CH01100P._CP'),
        ('ED6_DT07/CH01700._CH', 'ED6_DT07/CH01700P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
    ]

# id: 0x10002 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 20,
            z                   = 700,
            y                   = 39430,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 917510,
            chipIndex           = 6,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x1C2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1C2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1C2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1C2
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_1CE'),
        (-1, 'loc_210'),
    )

    def _loc_1CE(): pass

    label('loc_1CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1E1',
    )

    SetScenaFlags(ScenaFlag(0x00A2, 3, 0x513))
    Event(0, 0x000A)

    def _loc_1E1(): pass

    label('loc_1E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 1, 0x519)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 0, 0x518)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1FA',
    )

    SetMapFlags(0x10000000)
    Event(0, 0x000B)

    def _loc_1FA(): pass

    label('loc_1FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 1, 0x531)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 5, 0x52D)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20D',
    )

    SetScenaFlags(ScenaFlag(0x00A6, 1, 0x531))
    Event(0, 0x0010)

    def _loc_20D(): pass

    label('loc_20D')

    Jump('loc_210')

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_230',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -4500, 0, 6620, 99)

    Jump('loc_3E2')

    def _loc_230(): pass

    label('loc_230')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_250',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -4500, 0, 6620, 99)

    Jump('loc_3E2')

    def _loc_250(): pass

    label('loc_250')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_270',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -4500, 0, 6620, 99)

    Jump('loc_3E2')

    def _loc_270(): pass

    label('loc_270')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_2A6',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -4500, 0, 6620, 99)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x000C, -90, 0, 9830, 355)

    Jump('loc_3E2')

    def _loc_2A6(): pass

    label('loc_2A6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_2CD',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 670, 0, 8480, 6)
    CreateThread(0x000D, 0x00, 0x00, 0x0003)

    Jump('loc_3E2')

    def _loc_2CD(): pass

    label('loc_2CD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2D7',
    )

    Jump('loc_3E2')

    def _loc_2D7(): pass

    label('loc_2D7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_332',
    )

    SetChrPos(0x000E, 40, 800, 11550, 0)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrPos(0x0008, 140, 0, 12690, 175)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 3, 0x51B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_32F',
    )

    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -130, 0, 10450, 0)

    def _loc_32F(): pass

    label('loc_32F')

    Jump('loc_3E2')

    def _loc_332(): pass

    label('loc_332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            Expr.Return,
        ),
        'loc_37E',
    )

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, -100, 0, 12700, 180)
    SetChrPos(0x0008, -2310, 0, 14200, 0)
    SetChrPos(0x000E, 40, 800, 11550, 0)
    ClearChrFlags(0x000E, 0x0080)

    Jump('loc_3E2')

    def _loc_37E(): pass

    label('loc_37E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Return,
        ),
        'loc_3A5',
    )

    ClearChrFlags(0x0008, 0x0080)
    CreateThread(0x0008, 0x00, 0x00, 0x0002)
    SetChrPos(0x0008, 140, 0, 12690, 175)

    Jump('loc_3E2')

    def _loc_3A5(): pass

    label('loc_3A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_3C5',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -4500, 0, 6620, 99)

    Jump('loc_3E2')

    def _loc_3C5(): pass

    label('loc_3C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_3E2',
    )

    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000B, -4500, 0, 6620, 99)

    def _loc_3E2(): pass

    label('loc_3E2')

    Return()

# id: 0x0001 offset: 0x3E3
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A7, 2, 0x53A)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 0, 0x558)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3FB',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_428')

    def _loc_3FB(): pass

    label('loc_3FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_413',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_428')

    def _loc_413(): pass

    label('loc_413')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_428',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_428(): pass

    label('loc_428')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 4, 0x52C)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_48A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 2, 0x532)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 2, 0x54A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_48A',
    )

    LoadEffect(0x01, 'map\\\\mpfog.eff')
    PlayEffect(0x01, 0x01, 0x00FF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_48A(): pass

    label('loc_48A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_496',
    )

    OP_72(0x0000, 0x0004)

    def _loc_496(): pass

    label('loc_496')

    Return()

# id: 0x0002 offset: 0x497
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4AC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_4AC(): pass

    label('loc_4AC')

    Return()

# id: 0x0003 offset: 0x4AD
@scena.Code('func_03_4AD')
def func_03_4AD():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4D0',
    )

    OP_8D(0x00FE, -1710, 9770, 3200, 6310, 3000)

    Jump('func_03_4AD')

    def _loc_4D0(): pass

    label('loc_4D0')

    Return()

# id: 0x0004 offset: 0x4D1
@scena.Code('func_04_4D1')
def func_04_4D1():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 6, 0x536)),
            Expr.Return,
        ),
        'loc_4EE',
    )

    PlaySE(402, 0x00, 0x64)

    ChrTalk(
        0x00FE,
        (
            '喵～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4EE(): pass

    label('loc_4EE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x4F2
@scena.Code('func_05_4F2')
def func_05_4F2():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_5EB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_57F',
    )

    ChrTalk(
        0x00FE,
        (
            '拉赛尔博士\n',
            '好像已经回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我本来还想请他\n',
            '给我们多提一些建议的，\n',
            '这次还是算了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只能以后有机会再说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5EB')

    def _loc_57F(): pass

    label('loc_57F')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '哦？\n',
            '拉赛尔博士好像已经回去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次这么早就\n',
            '结束了研究工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '真的是难得一见呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5EB(): pass

    label('loc_5EB')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x5EF
@scena.Code('func_06_5EF')
def func_06_5EF():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_700',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_65B',
    )

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '拉赛尔博士到底去了哪里呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我倒是希望他能够\n',
            '好好地收拾一下试验用具。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6FD')

    def _loc_65B(): pass

    label('loc_65B')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '现在我正在重新\n',
            '对导力枪进行设计……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过还是有些不舍得\n',
            '对已经成熟的设计\n',
            '做大幅度的改动啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼……这下子\n',
            '说不定会比从图纸开始\n',
            '重新设计还要麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6FD(): pass

    label('loc_6FD')

    Jump('loc_149A')

    def _loc_700(): pass

    label('loc_700')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_7D6',
    )

    ChrTalk(
        0x00FE,
        (
            '现在处于研究阶段的导力枪的\n',
            '平衡性出了一些问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，如果能够做得更加易用，\n',
            '说不定会成为十分畅销的商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底是注重性能，\n',
            '还是注重易用性呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这个抉择太难了，\n',
            '还是先考虑二者兼顾吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_149A')

    def _loc_7D6(): pass

    label('loc_7D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 1, 0x559)),
            Expr.Return,
        ),
        'loc_9C7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_8C8',
    )

    ChrTalk(
        0x00FE,
        (
            '为了下一次的研究，\n',
            '我已经开始整理相关资料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次应该会以易用性\n',
            '作为追求的目标吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实老实说，\n',
            '到底应该注重哪一方面的设计\n',
            '连我自己也不是很清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因如此，对我们技术人员来说，\n',
            '这一难题才有挑战的价值。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C4')

    def _loc_8C8(): pass

    label('loc_8C8')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哟，早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '从昨天开始，\n',
            '我就在整理关于下一次研究主题的资料了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这次应该会以易用性\n',
            '作为追求的目标吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '其实老实说，\n',
            '到底应该注重哪一方面的设计\n',
            '连我自己也不是很清楚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因如此，对我们技术人员来说，\n',
            '这一难题才有挑战的价值。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9C4(): pass

    label('loc_9C4')

    Jump('loc_149A')

    def _loc_9C7(): pass

    label('loc_9C7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AA, 0, 0x550)),
            Expr.Return,
        ),
        'loc_C2E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_ADB',
    )

    ChrTalk(
        0x00FE,
        (
            '今天，有位客人在维修柜台\n',
            '打听易用的照相机，\n',
            '我就向其介绍了相关的商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，易用这一特性\n',
            '用数字是表现不出来的。\n',
            '结果我还是没有办法说清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然武器店的老板\n',
            '叮嘱我说要基于\n',
            '能让更多人使用这一点来考虑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我还是不能理解\n',
            '他这句话的含义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C2B')

    def _loc_ADB(): pass

    label('loc_ADB')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '……唉，真难办啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今天，我在维修柜台\n',
            '向一位客人介绍了相关的商品……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我不管怎么介绍商品的高性能，\n',
            '也不能使客人满意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像那位客人想要的是\n',
            '使用起来非常方便的照相机……\n',
            '不过易用性用数字是表现不出来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然武器店的老板\n',
            '叮嘱我说要基于\n',
            '能让更多人使用这一点来考虑……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我还是不能理解\n',
            '他这句话的含义。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C2B(): pass

    label('loc_C2B')

    Jump('loc_149A')

    def _loc_C2E(): pass

    label('loc_C2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A1, 6, 0x50E)),
            Expr.Return,
        ),
        'loc_10E0',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_1023',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 5, 0x585)),
            Expr.Return,
        ),
        'loc_D2C',
    )

    ChrTalk(
        0x00FE,
        (
            '导力枪的研究\n',
            '我觉得还算是比较顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一些细节部分\n',
            '看来还需要些时间来完善，\n',
            '但是不管怎么说大体已经成形了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这个势头研发的话，\n',
            '会比我预计的更早出现在商店货架上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且发售的时候\n',
            '商品也会包装得更可爱一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1020')

    def _loc_D2C(): pass

    label('loc_D2C')

    SetScenaFlags(ScenaFlag(0x00B0, 5, 0x585))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D80',
    )

    ChrTalk(
        0x00FE,
        (
            '啊，提妲。\n',
            '哎，还有这几位……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D98')

    def _loc_D80(): pass

    label('loc_D80')

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D98(): pass

    label('loc_D98')

    ChrTalk(
        0x0101,
        (
            '#501F嗯？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们好像\n',
            '在卢安见过面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，果然是你们呀。\n',
            '那时候真是给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '来，要不要看看\n',
            '我做的导力枪的试验品啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F啊，我也想起来了。\n',
            '你就是那时候的学者。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#560F对了，\n',
            '加鲁诺先生，您好像说过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在去卢安的途中\n',
            '把导力枪试制品丢掉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0107, 400)

    ChrTalk(
        0x00FE,
        (
            '哎呀～\n',
            '那一次可真是被逼到绝路了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真的是得救了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F在那之后\n',
            '你的研究进行得如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '我觉得还算是比较顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一些细节部分\n',
            '看来还需要些时间来完善，\n',
            '但是不管怎么说大体已经成形了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这个势头研发的话，\n',
            '会比我预计的更早出现在商店货架上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且发售的时候\n',
            '商品也会包装得更可爱一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1020(): pass

    label('loc_1020')

    Jump('loc_10DD')

    def _loc_1023(): pass

    label('loc_1023')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1073',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '现在可不是发呆的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要赶快把改良方案\n',
            '确定下来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10DD')

    def _loc_1073(): pass

    label('loc_1073')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼～……\n',
            '露依赛重新把试制品做了出来，\n',
            '真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有样品的话，\n',
            '研究就没办法进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10DD(): pass

    label('loc_10DD')

    Jump('loc_149A')

    def _loc_10E0(): pass

    label('loc_10E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_149A',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0022, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_13E0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00B0, 5, 0x585)),
            Expr.Return,
        ),
        'loc_11DE',
    )

    ChrTalk(
        0x00FE,
        (
            '导力枪的研究\n',
            '我觉得还算是比较顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一些细节部分\n',
            '看来还需要些时间来完善，\n',
            '但是不管怎么说大体已经成形了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这个势头研发的话，\n',
            '会比我预计的更早出现在商店货架上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且发售的时候\n',
            '商品也会包装得更可爱一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_13DD')

    def _loc_11DE(): pass

    label('loc_11DE')

    SetScenaFlags(ScenaFlag(0x00B0, 5, 0x585))

    ChrTalk(
        0x00FE,
        (
            '哎呀，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F嗯？怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F说起来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们好像\n',
            '在卢安见过面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '啊，我记起来了。\n',
            '那时候真是给你们添麻烦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x00FE, 0x0101, 400)

    ChrTalk(
        0x00FE,
        (
            '来，要不要看看我做的\n',
            '导力枪的试验品啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#001F啊，我也想起来了。\n',
            '你就是那时候的学者。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F在那之后\n',
            '你的研究进行得如何了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嗯，\n',
            '我觉得还算是比较顺利吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '一些细节部分\n',
            '看来还需要些时间来完善，\n',
            '但是不管怎么说大体已经成形了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '照这个势头研发的话，\n',
            '会比我预计的更早出现在商店货架上哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且发售的时候\n',
            '商品也会包装得更可爱一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13DD(): pass

    label('loc_13DD')

    Jump('loc_149A')

    def _loc_13E0(): pass

    label('loc_13E0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1430',
    )

    ChrTalk(
        0x00FE,
        (
            '唉，\n',
            '现在可不是发呆的时候。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '要赶快把改良方案\n',
            '确定下来才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_149A')

    def _loc_1430(): pass

    label('loc_1430')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '呼～……\n',
            '露依赛重新把试制品做了出来，\n',
            '真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有样品的话，\n',
            '研究就没办法进行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_149A(): pass

    label('loc_149A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x149E
@scena.Code('func_07_149E')
def func_07_149E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_1550',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 3, 0x51B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1500',
    )

    ChrTalk(
        0x000A,
        (
            '#0550071595V#800F提妲就拜托你们照顾了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071596V提妲，\n',
            '去的时候要当心哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1550')

    def _loc_1500(): pass

    label('loc_1500')

    ChrTalk(
        0x000A,
        (
            '#0550071597V#800F咦，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071598V去亚尔摩村的话，\n',
            '要从西南方的门口出城啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1550(): pass

    label('loc_1550')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x1554
@scena.Code('func_08_1554')
def func_08_1554():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_15F1',
    )

    ChrTalk(
        0x0008,
        (
            '#0540071590V#100F抱歉，亚尔摩村水泵修理的工作\n',
            '就麻烦你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071591V只要把提妲送到那里，\n',
            '后面的工作交给她就行了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071592V那么，就拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1652')

    def _loc_15F1(): pass

    label('loc_15F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 3, 0x513)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 1, 0x511)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1652',
    )

    ChrTalk(
        0x0008,
        (
            '#0540071593V#100F嗯？在干什么呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071594V还不快点去把\n',
            '内燃引擎设备和汽油拿到这里来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1652(): pass

    label('loc_1652')

    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x1656
@scena.Code('func_09_1656')
def func_09_1656():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0009,
        (
            '#0070071299V#060F内燃引擎设备和汽油的保管地方，\n',
            '去五楼的演算室问问就知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A2, 6, 0x516)),
            Expr.Return,
        ),
        'loc_16ED',
    )

    ChrTalk(
        0x0101,
        (
            '#0010071300V#000F嗯，保管地点已经知道了，\n',
            '我们马上去拿过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_172F')

    def _loc_16ED(): pass

    label('loc_16ED')

    ChrTalk(
        0x0101,
        (
            '#0010071301V#505F五楼的演算室吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071302V#000F那我们先去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_172F(): pass

    label('loc_172F')

    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x1733
@scena.Code('func_0A_1733')
def func_0A_1733():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-770, 0, 1240, 0)
    FormationDelMember(0x06, 0xFF)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    OP_4A(0x0009, 255)
    OP_4A(0x0008, 255)
    SetChrPos(0x0008, -100, 0, 12700, 180)
    SetChrPos(0x0009, -1030, 0, 1690, 0)
    SetChrPos(0x0101, -600, 0, 510, 0)
    SetChrPos(0x0102, -1950, 0, 750, 0)
    SetChrPos(0x000E, 40, 800, 11550, 0)
    ClearChrFlags(0x000E, 0x0080)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540071212V唉！又失败了吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_17E7')
    def lambda_17E7():
        CameraMove(1050, 0, 11840, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_17E7)

    @scena.Lambda('lambda_17FF')
    def lambda_17FF():
        ChrWalkTo(0x00FE, 1370, 0, 9940, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_17FF)

    Sleep(300)

    @scena.Lambda('lambda_181F')
    def lambda_181F():
        ChrWalkTo(0x00FE, -800, 0, 10000, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_181F)

    Sleep(200)

    @scena.Lambda('lambda_183F')
    def lambda_183F():
        ChrWalkTo(0x00FE, 130, 0, 9790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_183F)

    WaitForThreadExit(0x0009, 0x0001)
    ChrTurnDirection(0x0009, 0x0008, 0)

    ChrTalk(
        0x0009,
        (
            '#0070071213V#560F爷爷。\n',
            '我们来帮忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071214V#103F哦哦，提妲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071215V哦……\n',
            '你们也都来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071216V#506F嘿嘿～\n',
            '我们也很在意嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071217V#006F对了，现在到底在干什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071218V#104F如你们所见，\n',
            '我正在尝试用工作机器把\n',
            '『黑色导力器』的外壳切开……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071219V看来也并不顺利啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071220V#014F怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071221V#102F百闻不如一见，你们亲眼看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071222V……按下按钮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(156, 0x00, 0x64)
    Sleep(400)

    PlaySE(224, 0x00, 0x64)
    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_70(0x0001, 3)
    OP_70(0x0002, 3)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010071223V#004F哇……这是什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070071224V#062F工作用的圆盘锯。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071225V由特殊合金制成的，\n',
            '能切断绝大多数种类的材料……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071226V#501F哦，用这个的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0001, 3)
    OP_6F(0x0002, 3)
    OP_70(0x0001, 37)
    OP_70(0x0002, 37)
    OP_73(0x0001)
    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0001, 34)
    OP_6F(0x0002, 34)
    OP_70(0x0001, 37)
    OP_70(0x0002, 37)
    PlaySE(199, 0x00, 0x64)
    LoadEffect(0x00, 'map\\\\mp007_00.eff')
    PlayEffect(0x00, 0x00, 0x000E, 0, 300, 0, 0, 0, 0, 300, 300, 300, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_23(0x00E0)
    OP_23(0x00C7)
    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    OP_73(0x0001)
    Sleep(500)

    StopEffect(0x00, 0x02)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010071227V#004F停、停下来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070071228V#561F果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071229V#012F虽然规模较小，不过是和昨天一样的现象。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071230V#102F看来，这个黑色的东西能让\n',
            '打算对其进行干涉的导力器的机能\n',
            '完全停止下来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071231V不仅仅是熄灭照明设备，\n',
            '其他的导力器也会被停止下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071232V#002F是、是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070071233V#064F但是，爷爷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071234V为什么没有像昨天那样\n',
            '影响到其他的范围呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071235V#101F嗯，你发现得好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071236V这个停止现象\n',
            '似乎会在周围运作的导力器中\n',
            '产生连锁反应而扩大。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071237V#100F有效范围大概为５亚矩。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071238V反过来说，\n',
            '如果范围内没有运作中的导力器，\n',
            '此现象就不能再继续扩大了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071239V#014F原来如此……\n',
            '还有这样的定律啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071240V#104F但是，就算知道了这一点，\n',
            '关键的机器不能运转，\n',
            '还是无法调查导力器的内部呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071241V这才是真正的麻烦所在呀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071242V#006F不能想办法\n',
            '用人力切开这个东西吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071243V比如说靠气势或毅力之类的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071244V#018F你还真敢说啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071245V用特殊合金制的小刀划过\n',
            '不是也没有伤痕吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071246V#505F啊，也是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071247V#006F嗯～那么用火呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071248V放进熔铁炉里熔掉怎么样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070071249V#065F那、那种做法，\n',
            '内部的零件也会坏掉的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071250V#007F果然不行吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071251V#103F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071252V不，也许行得通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071253V#004F哎哎！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071254V#014F用高温熔化的方法吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071255V#102F不，不是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071256V问题在于导力——\n',
            '我们太依赖靠导力来运作的机器了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071257V用导力以外的能量\n',
            '来运作工作机器就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071258V#505F用导力以外的能量\n',
            '来运作……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071259V#010F有这样的方法吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071260V#104F所谓的『内燃引擎』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071261V是利用火燃烧\n',
            '所产生的能量来运作的装置。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071262V这项发明的历史比导力器更为悠久，\n',
            '但效率也比导力引擎要低。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071263V#100F不过，简单地使工作机器运作，\n',
            '这种程度还是可以做得到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071264V#004F还有那样的东西啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071265V#019F原来如此，\n',
            '这就是用『火』吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070071266V#064F但是，爷爷。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071267V内燃引擎这个设备，\n',
            '我看都没看过呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071268V#100F记得在中央工房某个地方\n',
            '保存有研究用的设备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071269V#103F对了，\n',
            '还必须找到燃料。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071270V#000F燃料……是油吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071271V#100F那还远远不够，\n',
            '必须要用『汽油』那样燃烧力更强的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071272V以前这东西曾经作为溶剂使用过，\n',
            '说不定还有剩余下来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071273V唔……\n',
            '好像行得通。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071274V#101F就这样定了！\n',
            '赶快开始改造工作机器吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070071275V#560F啊，我也来帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071276V#006F那个那个，\n',
            '有我们能帮上忙的地方吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071277V虽然做不到\n',
            '像提妲那样专业的工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071278V#100F这样的话，\n',
            '你们就去把那个内燃引擎和汽油取来吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071279V可能有点重，但以游击士的能力，\n',
            '我想你们应该能找到办法运过来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071280V#006FＯＫ，交给我们吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071281V#010F内燃引擎和汽油对吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071282V是放在哪里的呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071283V#103F嗯？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071284V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071285V…………哎呀…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071286V#014F博士您该不会是\n',
            '忘了放在哪里了吧……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071287V#104F嗯，忘了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071288V#509F还回答得这么轻描淡写～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '#0070071289V#560F#2P那、那个，艾丝蒂尔姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071290V去演算室的话，\n',
            '我想应该能查到放在哪儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0009, 400)
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071291V#505F演算室？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070071292V#060F#2P五楼有个房间里\n',
            '放着一台导力演算器。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071293V有关中央工房的资料\n',
            '全部都记录在那机器里面，\n',
            '我想应该也有各种设备的保管场所吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071294V#014F好厉害。\n',
            '竟然有这样的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071295V#101F就是这样，拜托你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071296V#007F真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071297V#006F算了，\n',
            '总之先到五楼的演算室去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071298V#010F嗯，走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003F, 0x01, 0x0080)
    OP_28(0x003F, 0x01, 0x0100)
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0101, -410, 0, 8910, 180)
    SetChrPos(0x0102, -410, 0, 8910, 180)
    SetChrPos(0x0009, -100, 0, 12700, 180)
    SetChrPos(0x0008, -2310, 0, 14200, 0)
    OP_4B(0x0008, 255)
    CreateThread(0x0009, 0x00, 0x00, 0x0002)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_69(0x0101, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x28E0
@scena.Code('func_0B_28E0')
def func_0B_28E0():
    FormationAddMember(0x06, 0xFF)
    EventBegin(0x00)
    CameraMove(600, 0, 11100, 0)
    ClearChrFlags(0x0008, 0x0080)
    OP_4A(0x0008, 255)
    OP_4A(0x000A, 255)
    SetChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 400, 0, 10200, 270)
    SetChrPos(0x0107, -630, 0, 10390, 90)
    SetChrPos(0x0101, 640, 0, 800, 0)
    SetChrPos(0x0102, -430, 0, 800, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010071500V#1P呼，我们回来了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_297C')
    def lambda_297C():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_297C)

    @scena.Lambda('lambda_298A')
    def lambda_298A():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_298A)

    @scena.Lambda('lambda_2998')
    def lambda_2998():
        ChrWalkTo(0x00FE, 640, 0, 8970, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2998)

    Sleep(500)

    ChrWalkTo(0x0102, -430, 0, 8740, 3000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020071501V#010F博士，\n',
            '需要的东西都带来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071502V#103F#5P哦哦，回来啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071503V#560F#1P辛苦你们了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '内燃引擎设备',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '交出了',
            (TxtCtl.SetColor, 0x2),
            '汽油罐',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    RemoveItem(0x0367, 1)
    RemoveItem(0x0368, 1)

    ChrTalk(
        0x0101,
        (
            '#0010071504V#007F呼～\n',
            '的确是有点重啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071505V#101F#5P哦哦，真是辛苦啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071506V#100F哈哈，告诉你们，\n',
            '工作机器也刚好改造完毕了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071507V之后只要装上内燃引擎，\n',
            '再灌入汽油就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#0540071508V#100F#5P提妲，\n',
            '我们快点完成它吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070071509V#061F#1P好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(500)

    CameraMove(-1390, 0, 11640, 0)
    SetChrPos(0x0101, -2690, 0, 9810, 0)
    SetChrPos(0x0102, -1580, 0, 9760, 0)
    SetChrPos(0x0107, -3220, 0, 11360, 90)
    SetChrPos(0x0008, -2350, 0, 13080, 180)
    OP_72(0x0000, 0x0004)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0540071510V#101F好了，完成啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071511V#501F呜哇～\n',
            '这东西真特别啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010071512V这就是利用内燃引擎的引擎吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071513V#060F嗯，是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071514V引擎里面燃烧着汽油，\n',
            '所释放的能量就能使工作机器运作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071515V#010F这样一来，即使不依靠导力，\n',
            '也能运行工作机器了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071516V#104F没错。\n',
            '那么赶快打开开关吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x01, 0x00, 0x000C)
    CreateThread(0x0102, 0x01, 0x00, 0x000D)
    CreateThread(0x0101, 0x01, 0x00, 0x000E)
    CreateThread(0x0107, 0x01, 0x00, 0x000F)
    CameraMove(1050, 0, 11840, 2000)
    WaitForThreadExit(0x0107, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#0540071517V#102F……按下按钮。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(156, 0x00, 0x64)
    Sleep(400)

    PlaySE(159, 0x01, 0x64)

    @scena.Lambda('lambda_2DE1')
    def lambda_2DE1():
        OP_7C(0, 10, 3000, 100)
        Yield()

        Jump('lambda_2DE1')

    DispatchAsync2(0x0101, 0x0003, lambda_2DE1)

    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_70(0x0001, 3)
    OP_70(0x0002, 3)
    Sleep(500)

    SetChrDirection(0x0008, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010071518V#004F哇，动了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071519V#010F和导力引擎相比，\n',
            '噪音和振动都要大很多啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071520V#102F嗯，这是它的缺点之一。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071521V但和预想的一样，\n',
            '应该不用担心会发生昨天的事情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071522V那么，就这样开始解体吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071523V#002F……（吞口水）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071524V#560F……（紧张紧张）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0001, 3)
    OP_6F(0x0002, 3)
    OP_70(0x0001, 45)
    OP_70(0x0002, 45)
    OP_73(0x0001)
    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0001, 42)
    OP_6F(0x0002, 42)
    OP_70(0x0001, 45)
    OP_70(0x0002, 45)
    PlaySE(199, 0x01, 0x64)
    LoadEffect(0x00, 'map\\\\mp010_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -100, 1200, 11450, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010071525V#004F哇哇……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071526V#012F好厉害的火花……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071527V#102F好，先停一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071528V首先要确认一下\n',
            '这东西外壳的削损程度。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    StopEffect(0x00, 0x02)
    OP_23(0x00C7)
    TerminateThread(0x0101, 0x03)
    PlaySE(154, 0x00, 0x64)
    OP_23(0x009F)
    OP_7C(0, 100, 3000, 100)
    OP_6F(0x0001, 362)
    OP_6F(0x0002, 362)
    OP_70(0x0001, 365)
    OP_70(0x0002, 365)
    OP_73(0x0001)
    Sleep(1000)

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们往黑色导力器外壳的表面上看去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '外壳上只是留下了小小的伤口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010071529V#505F只、只削了这么一点？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071530V#065F真不敢相信……\n',
            '这可是特殊合金制的圆盘锯呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071531V#012F真是极为坚硬的材质啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071532V#101F其实只要保持耐心继续下去，\n',
            '应该能完全切开的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071533V哈哈……\n',
            '只可惜圆盘锯有必要多换几个了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071534V#006F这么说……\n',
            '从现在开始就是耐力的考验了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x000A, -800, 0, 800, 0)

    ChrTalk(
        0x000A,
        (
            '#0550071535V#1P博士，你有空吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_328F')
    def lambda_328F():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_328F)

    @scena.Lambda('lambda_329D')
    def lambda_329D():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_329D)

    @scena.Lambda('lambda_32AB')
    def lambda_32AB():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_32AB)

    @scena.Lambda('lambda_32B9')
    def lambda_32B9():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_32B9)

    ChrWalkTo(0x000A, -150, 0, 8000, 3000, 0x00)

    ChrTalk(
        0x000A,
        (
            '#0550071536V#801F哦哦……\n',
            '已经顺利改造完毕了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071537V#104F当然了，\n',
            '你以为我是谁呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071538V#100F怎么了，\n',
            '又有什么麻烦吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550071539V#800F刚才亚尔摩旅馆  \n',
            '给博士发了一条联络过来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071540V他们说旅馆那个抽取温泉的导力泵\n',
            '好像出了故障。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0550071541V这样下去的话就不能营业了，\n',
            '所以想请博士马上过去修理一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071542V#102F啊～怎么搞的！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071543V哎呀呀！\n',
            '如此忙的时候还来麻烦的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550071544V#805F这样的话……\n',
            '要不要我派其他技师代替你去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071545V#100F不……\n',
            '那是４０多年前的破铜烂铁了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071546V只熟悉最新型机械的年轻人\n',
            '是没办法应付那东西的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071547V#104F唔，真是伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 1700, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0107)
    ChrTurnDirection(0x0107, 0x0008, 400)

    ChrTalk(
        0x0107,
        (
            '#0070071548V#560F那个，爷爷……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071549V我有个建议……\n',
            '这次让我替您去修理好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_359C')
    def lambda_359C():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_359C)

    @scena.Lambda('lambda_35AA')
    def lambda_35AA():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_35AA)

    ChrTurnDirection(0x0008, 0x0107, 400)

    ChrTalk(
        0x0008,
        (
            '#0540071550V#103F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550071551V#802F提妲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071552V#060F以前您带我去的时候，\n',
            '我也帮忙维修过那东西哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071553V所以我想没问题的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071554V#100F唔……的确。\n',
            '技术方面交给你应该没问题……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540071555V不过我担心别的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550071556V#803F是啊，\n',
            '街道上有那么多魔兽出没……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071557V#063F可是可是……\n',
            '毛婆婆有麻烦，我不能置之不理啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_370F')
    def lambda_370F():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_370F)

    ChrTurnDirection(0x0101, 0x0102, 400)
    OP_62(0x0101, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    OP_62(0x0102, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x0101)
    OP_63(0x0102)

    @scena.Lambda('lambda_3753')
    def lambda_3753():
        ChrTurnDirection(0x00FE, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3753)

    ChrTurnDirection(0x0101, 0x0107, 400)

    ChrTalk(
        0x0101,
        (
            '#0010071558V#006F#2P……那样的话，\n',
            '交给我们两个不就行了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0101, 400)

    ChrTalk(
        0x0107,
        (
            '#0070071559V#064F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071560V#010F#2P艾丝蒂尔说的没错。\n',
            '确保道路安全也是游击士的义务。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020071561V这次就让我们两个做护卫吧。\n',
            '我们一定会将提妲安全护送到那里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550071562V#801F哦哦，你们一起去的话，\n',
            '那就没什么好担心的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071563V#100F唔……\n',
            '难得你们费心，那就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071564V#065F那个那个……\n',
            '这样麻烦你们可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010071565V#006F#2P哎呀～小孩子就不要担心太多啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020071566V#019F#2P一起去的话起码多个照应。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070071567V#067F谢、谢谢你们。\n',
            '艾丝蒂尔姐姐、约修亚哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0107, 0x0008, 400)
    Sleep(200)

    ChrTurnDirection(0x0107, 0x000A, 400)
    Sleep(500)

    ChrTalk(
        0x0107,
        (
            '#0070071568V#560F爷爷，工房长叔叔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070071569V那我们走了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0540071570V#101F哦哦，拜托你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0550071571V#801F路上要小心点哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(-100, 0, 6770, 0)
    SetChrPos(0x0101, -100, 0, 6770, 180)
    SetChrPos(0x0102, -100, 0, 6770, 180)
    SetChrPos(0x0107, -100, 0, 6770, 180)
    SetChrPos(0x0008, 0, 0, 12740, 180)
    SetChrPos(0x000A, -130, 0, 10450, 0)
    OP_4B(0x0008, 255)
    OP_4B(0x000A, 255)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    Sleep(500)

    FadeIn(1000, 0)
    ClearMapFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00A3, 2, 0x51A))
    OP_28(0x003F, 0x04, 0x10)
    OP_28(0x003F, 0x04, 0x20)
    OP_28(0x0040, 0x04, 0x02)
    OP_28(0x0040, 0x04, 0x04)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x3AD0
@scena.Code('func_0C_3AD0')
def func_0C_3AD0():
    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -1930, 0, 13450, 2000, 0x00)
    ChrWalkTo(0x00FE, -270, 0, 13940, 2000, 0x00)
    ChrWalkTo(0x00FE, -100, 0, 12700, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 90, 400)

    Return()

# id: 0x000D offset: 0x3B1E
@scena.Code('func_0D_3B1E')
def func_0D_3B1E():
    Sleep(400)

    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 1140, 0, 10100, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 315, 400)

    Return()

# id: 0x000E offset: 0x3B49
@scena.Code('func_0E_3B49')
def func_0E_3B49():
    Sleep(800)

    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 120, 0, 9950, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x3B74
@scena.Code('func_0F_3B74')
def func_0F_3B74():
    Sleep(1200)

    SetChrFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, -3000, 0, 9870, 2000, 0x00)
    ChrWalkTo(0x00FE, -740, 0, 10210, 2000, 0x00)
    ClearChrFlags(0x00FE, 0x0004)
    SetChrDirection(0x00FE, 0, 400)

    Return()

# id: 0x0010 offset: 0x3BB3
@scena.Code('func_10_3BB3')
def func_10_3BB3():
    EventBegin(0x00)
    CameraMove(-180, 0, 2620, 0)
    SetMapFlags(0x40000000)
    FormationAddMember(0x05, 0xFF)
    SetChrStatus(0x0005, 0x00, 26)
    OP_B5(0x0005, 0x00)
    OP_B5(0x0005, 0x01)
    OP_B5(0x0005, 0x02)
    OP_B5(0x0005, 0x03)
    EquipCmd(0x05, 0x009B)
    EquipCmd(0x05, 0x00F5)
    EquipCmd(0x05, 0x0113)
    EquipCmd(0x05, 0x025F, 0x00)
    EquipCmd(0x05, 0x0259, 0x01)
    EquipCmd(0x05, 0x0262, 0x02)
    AddCraft(0x0005, 0x00C8)
    AddCraft(0x0005, 0x00C9)
    AddCraft(0x0005, 0x00CA)
    AddSCraft(0x0005, 0x00FF)
    AddSCraft(0x0005, 0x0100)
    SetChrFlags(0x0106, 0x0080)
    SetChrPos(0x0107, -850, 0, 2040, 0)
    SetChrPos(0x0101, -1590, 0, 900, 0)
    SetChrPos(0x0102, -260, 0, 1060, 0)
    PlaySE(159, 0x01, 0x64)

    @scena.Lambda('lambda_3C55')
    def lambda_3C55():
        OP_7C(0, 10, 3000, 100)
        Yield()

        Jump('lambda_3C55')

    DispatchAsync2(0x0101, 0x0003, lambda_3C55)

    OP_71(0x0001, 0x0020)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0001, 42)
    OP_6F(0x0002, 42)
    OP_70(0x0001, 45)
    OP_70(0x0002, 45)
    FadeIn(2000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070080754V#062F爷爷，不好了啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080755V#064F……啊……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(1770, 0, 12830, 2000)

    @scena.Lambda('lambda_3CF1')
    def lambda_3CF1():
        ChrWalkTo(0x00FE, 320, 0, 9630, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3CF1)

    @scena.Lambda('lambda_3D0C')
    def lambda_3D0C():
        ChrWalkTo(0x00FE, -850, 0, 8690, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3D0C)

    @scena.Lambda('lambda_3D27')
    def lambda_3D27():
        ChrWalkTo(0x00FE, 950, 0, 8560, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3D27)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010080756V#004F奇怪了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010080757V既然博士不在的话，\n',
            '为什么工作机器自己会在动？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080758V#065F是、是啊……\n',
            '总之先把工作机器停下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3DD2')
    def lambda_3DD2():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_3DD2')

    DispatchAsync2(0x0101, 0x0001, lambda_3DD2)

    @scena.Lambda('lambda_3DE3')
    def lambda_3DE3():
        ChrTurnDirection(0x00FE, 0x0107, 400)
        Yield()

        Jump('lambda_3DE3')

    DispatchAsync2(0x0102, 0x0001, lambda_3DE3)

    SetChrFlags(0x0107, 0x0004)
    ChrWalkTo(0x0107, 2430, 0, 10010, 4000, 0x00)
    ChrWalkTo(0x0107, 2620, 0, 12910, 4000, 0x00)
    ChrWalkTo(0x0107, 80, 0, 13580, 4000, 0x00)
    ChrWalkTo(0x0107, 140, 0, 12800, 4000, 0x00)
    SetChrDirection(0x0107, 90, 400)
    Sleep(500)

    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_23(0x009F)
    TerminateThread(0x0101, 0x03)
    PlaySE(154, 0x00, 0x64)
    OP_7C(0, 100, 3000, 100)
    OP_6F(0x0001, 362)
    OP_6F(0x0002, 362)
    OP_70(0x0001, 365)
    OP_70(0x0002, 365)
    OP_73(0x0001)
    Sleep(1500)

    ChrTalk(
        0x0107,
        (
            '#0070080759V#561F呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070080760V#063F爷爷他……\n',
            '现在到底在哪儿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080761V#013F不止是博士……\n',
            '『黑色导力器』也不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080762V难道说这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0106, -790, 0, 2500, 0)
    ClearChrFlags(0x0106, 0x0080)

    ChrTalk(
        0x0106,
        (
            '#0050080763V#1P哼，你们在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_3F9E')
    def lambda_3F9E():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_3F9E)

    @scena.Lambda('lambda_3FAC')
    def lambda_3FAC():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3FAC)

    @scena.Lambda('lambda_3FBA')
    def lambda_3FBA():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3FBA)

    CameraMove(990, 0, 7840, 1000)

    ChrTalk(
        0x0101,
        (
            '#0010080764V#004F阿、阿加特！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080765V#014F您怎么会在这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_401D')
    def lambda_401D():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_401D')

    DispatchAsync2(0x0101, 0x0001, lambda_401D)

    @scena.Lambda('lambda_402E')
    def lambda_402E():
        ChrTurnDirection(0x00FE, 0x0106, 400)
        Yield()

        Jump('lambda_402E')

    DispatchAsync2(0x0102, 0x0001, lambda_402E)

    ChrWalkTo(0x0106, -210, 0, 6940, 3000, 0x00)
    CreateThread(0x0107, 0x02, 0x00, 0x0011)

    ChrTalk(
        0x0106,
        (
            '#0050080766V#552F哼，这句话是我问你们才对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050080767V我听到这里发生骚乱就赶了过来，\n',
            '不过没想到又被你们两个抢先一步。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050080768V真是不知天高地厚的小鬼，\n',
            '明明本事就不多，还到处乱出风头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080769V#509F你、你这个刀子嘴～……\n',
            '没见一段时间还是那么惹人厌啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0107, 0x0002)
    ChrTurnDirection(0x0107, 0x0106, 400)

    ChrTalk(
        0x0107,
        (
            '#0070080770V#064F那个……\n',
            '艾丝蒂尔姐姐你们认识他吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080771V#010F他叫阿加特。\n',
            '是我们在游击士协会的前辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTurnDirection(0x0106, 0x0107, 400)

    ChrTalk(
        0x0106,
        (
            '#0050080772V#052F喂，我问你们两个……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050080773V#057F既然全体人员已经疏散了，\n',
            '为什么还会有小鬼在这种地方？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0106, 1370, 0, 7480, 3000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '阿加特紧紧盯着提妲。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_62(0x0107, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0107,
        (
            '#0070080774V#065F……呜……',
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0107, 15, 0, 1000, 3000)
    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    ChrWalkTo(0x0101, 390, 0, 7670, 3000, 0x00)
    ChrTurnDirection(0x0101, 0x0106, 0)

    ChrTalk(
        0x0101,
        (
            '#0010080775V#009F等、等一下，\n',
            '你怎么吓唬人家女孩子啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050080776V#057F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050080777V#552F嘁……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050080778V虽然想说的话堆积如山，\n',
            '但还是以后再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050080779V#050F话说回来，这到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080780V#012F嗯，其实……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔他们向阿加特说明了拉赛尔博士不见的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0106,
        (
            '#0050080781V#053F唔，发烟筒吗……\n',
            '我有很不好的预感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050080782V#054F时间紧迫……\n',
            '赶快把博士找出来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010080783V#005F知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020080784V#012F明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070080785V#063F……爷爷……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_28(0x0041, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x4502
@scena.Code('func_11_4502')
def func_11_4502():
    ChrWalkTo(0x0107, 80, 0, 13580, 3000, 0x00)
    ChrWalkTo(0x0107, 830, 0, 13970, 3000, 0x00)
    ChrWalkTo(0x0107, 2620, 0, 12910, 3000, 0x00)
    ChrWalkTo(0x0107, 2260, 0, 7700, 3000, 0x00)
    ChrTurnDirection(0x0107, 0x0101, 400)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
