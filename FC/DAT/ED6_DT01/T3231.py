import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T3231_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3231   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拜舍尔'),
    TXT(0x02, '艾德'),
    TXT(0x03, '林'),
    TXT(0x04, '莉西亚'),
    TXT(0x05, '希利尔'),
    TXT(0x06, '艾缇'),
    TXT(0x07, '拉克'),
    TXT(0x08, '希玛'),
    TXT(0x09, '库安'),
    TXT(0x0A, '西加罗'),
    TXT(0x0B, '艾德尔'),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3231.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xF24
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
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01150._CH', 'ED6_DT07/CH01150P._CP'),
        ('ED6_DT07/CH01120._CH', 'ED6_DT07/CH01120P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01160._CH', 'ED6_DT07/CH01160P._CP'),
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01060._CH', 'ED6_DT07/CH01060P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
    ]

# id: 0x10002 offset: 0x102
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
            talkScenaIndex      = 0x0005,
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
            talkScenaIndex      = 0x0006,
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
            talkScenaIndex      = 0x0008,
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
            talkScenaIndex      = 0x0009,
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
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10003 offset: 0x262
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x262
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x262
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -1900,
            triggerZ            = 0,
            triggerY            = 5070,
            triggerRange        = 800,
            actorX              = -1900,
            actorZ              = 1000,
            actorY              = 5070,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -1890,
            triggerZ            = 0,
            triggerY            = -4990,
            triggerRange        = 800,
            actorX              = -1890,
            actorZ              = 1000,
            actorY              = -4990,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000F,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AA
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_2B4',
    )

    Jump('loc_36F')

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_2BE',
    )

    Jump('loc_36F')

    def _loc_2BE(): pass

    label('loc_2BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_2DE',
    )

    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -1080, 0, 440, 85)

    Jump('loc_36F')

    def _loc_2DE(): pass

    label('loc_2DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_2FE',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -1090, 0, -900, 82)

    Jump('loc_36F')

    def _loc_2FE(): pass

    label('loc_2FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_31E',
    )

    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, -1080, 0, 440, 85)

    Jump('loc_36F')

    def _loc_31E(): pass

    label('loc_31E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_328',
    )

    Jump('loc_36F')

    def _loc_328(): pass

    label('loc_328')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_332',
    )

    Jump('loc_36F')

    def _loc_332(): pass

    label('loc_332')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_352',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -990, 0, 10, 90)

    Jump('loc_36F')

    def _loc_352(): pass

    label('loc_352')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_36F',
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, -990, 0, 10, 90)

    def _loc_36F(): pass

    label('loc_36F')

    Return()

# id: 0x0001 offset: 0x370
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_388',
    )

    OP_B1('t3231_y')

    Jump('loc_391')

    def _loc_388(): pass

    label('loc_388')

    OP_B1('t3231_n')

    def _loc_391(): pass

    label('loc_391')

    OP_72(0x0008, 0x0010)
    OP_72(0x0009, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3AF',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)

    def _loc_3AF(): pass

    label('loc_3AF')

    Return()

# id: 0x0002 offset: 0x3B0
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_3C5(): pass

    label('loc_3C5')

    Return()

# id: 0x0003 offset: 0x3C6
@scena.Code('func_03_3C6')
def func_03_3C6():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_3D3',
    )

    Jump('loc_420')

    def _loc_3D3(): pass

    label('loc_3D3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_3DD',
    )

    Jump('loc_420')

    def _loc_3DD(): pass

    label('loc_3DD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_3E7',
    )

    Jump('loc_420')

    def _loc_3E7(): pass

    label('loc_3E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_3F1',
    )

    Jump('loc_420')

    def _loc_3F1(): pass

    label('loc_3F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_3FB',
    )

    Jump('loc_420')

    def _loc_3FB(): pass

    label('loc_3FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_405',
    )

    Jump('loc_420')

    def _loc_405(): pass

    label('loc_405')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_40F',
    )

    Jump('loc_420')

    def _loc_40F(): pass

    label('loc_40F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_419',
    )

    Jump('loc_420')

    def _loc_419(): pass

    label('loc_419')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_420',
    )

    def _loc_420(): pass

    label('loc_420')

    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x424
@scena.Code('func_04_424')
def func_04_424():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_431',
    )

    Jump('loc_52A')

    def _loc_431(): pass

    label('loc_431')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_43B',
    )

    Jump('loc_52A')

    def _loc_43B(): pass

    label('loc_43B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_491',
    )

    ChrTalk(
        0x00FE,
        (
            '蔡斯那边\n',
            '好像发生了什么大事件呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呼，\n',
            '早早地赶到这里真是明智啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52A')

    def _loc_491(): pass

    label('loc_491')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_49B',
    )

    Jump('loc_52A')

    def _loc_49B(): pass

    label('loc_49B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_505',
    )

    ChrTalk(
        0x00FE,
        (
            '嗯，真是好温泉。\n',
            '身体从内到外都感觉很暖和。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '泡温泉的时候\n',
            '可以把讨厌的事全都给忘掉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_52A')

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_50F',
    )

    Jump('loc_52A')

    def _loc_50F(): pass

    label('loc_50F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_519',
    )

    Jump('loc_52A')

    def _loc_519(): pass

    label('loc_519')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_523',
    )

    Jump('loc_52A')

    def _loc_523(): pass

    label('loc_523')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_52A',
    )

    def _loc_52A(): pass

    label('loc_52A')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x52E
@scena.Code('func_05_52E')
def func_05_52E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C0, 1, 0x601)),
            Expr.Return,
        ),
        'loc_53B',
    )

    Jump('loc_7BF')

    def _loc_53B(): pass

    label('loc_53B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AB, 5, 0x55D)),
            Expr.Return,
        ),
        'loc_545',
    )

    Jump('loc_7BF')

    def _loc_545(): pass

    label('loc_545')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A6, 7, 0x537)),
            Expr.Return,
        ),
        'loc_54F',
    )

    Jump('loc_7BF')

    def _loc_54F(): pass

    label('loc_54F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_63E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_5AB',
    )

    ChrTalk(
        0x00FE,
        (
            '原来如此，池钓吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '回到钓公师团的总部之后\n',
            '就立刻去找钓鱼场吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_63B')

    def _loc_5AB(): pass

    label('loc_5AB')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '呵呵，一大早就不由自主\n',
            '想来露天温泉泡个澡。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这里的浴池果然很大。\n',
            '有点像个池塘啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊，池塘吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '对了，\n',
            '下次试试池钓吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_63B(): pass

    label('loc_63B')

    Jump('loc_7BF')

    def _loc_63E(): pass

    label('loc_63E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 6, 0x526)),
            Expr.Return,
        ),
        'loc_648',
    )

    Jump('loc_7BF')

    def _loc_648(): pass

    label('loc_648')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 2, 0x522)),
            Expr.Return,
        ),
        'loc_652',
    )

    Jump('loc_7BF')

    def _loc_652(): pass

    label('loc_652')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 7, 0x51F)),
            Expr.Return,
        ),
        'loc_65C',
    )

    Jump('loc_7BF')

    def _loc_65C(): pass

    label('loc_65C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A3, 2, 0x51A)),
            Expr.Return,
        ),
        'loc_746',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_6C7',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然听说蔡斯\n',
            '没有什么好的钓鱼场……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过说不定恰恰会有\n',
            '没被人发现的好地方呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_743')

    def _loc_6C7(): pass

    label('loc_6C7')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '因为水泵坏了，\n',
            '温泉可能要暂时停业了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那个刚从王都来的小姐\n',
            '也很失望呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在泵修理好之前，\n',
            '我还是去钓鱼吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_743(): pass

    label('loc_743')

    Jump('loc_7BF')

    def _loc_746(): pass

    label('loc_746')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 2, 0x502)),
            Expr.Return,
        ),
        'loc_7BF',
    )

    ChrTalk(
        0x00FE,
        (
            '钓完鱼后泡澡\n',
            '果然是最舒服的事情的啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且还是温泉，\n',
            '真可以说是太幸福了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '啊啊，有点奢侈的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BF(): pass

    label('loc_7BF')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x7C3
@scena.Code('func_06_7C3')
def func_06_7C3():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0x7CA
@scena.Code('func_07_7CA')
def func_07_7CA():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0x7D1
@scena.Code('func_08_7D1')
def func_08_7D1():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0x7D8
@scena.Code('func_09_7D8')
def func_09_7D8():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000A offset: 0x7DF
@scena.Code('func_0A_7DF')
def func_0A_7DF():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000B offset: 0x7E6
@scena.Code('func_0B_7E6')
def func_0B_7E6():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x7ED
@scena.Code('func_0C_7ED')
def func_0C_7ED():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x7F4
@scena.Code('func_0D_7F4')
def func_0D_7F4():
    TalkBegin(0x00FE)
    TalkEnd(0x00FE)

    Return()

# id: 0x000E offset: 0x7FB
@scena.Code('func_0E_7FB')
def func_0E_7FB():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_809',
    )

    Call(0, 0x0010)

    Jump('loc_A30')

    def _loc_809(): pass

    label('loc_809')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 5, 0x525)),
            Expr.Return,
        ),
        'loc_97F',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '女浴室\n',
            '　需要使用的时候\n',
            '　请通知前台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_90F',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_884',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_88B')

    def _loc_884(): pass

    label('loc_884')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_88B(): pass

    label('loc_88B')

    ChrTalk(
        0x0102,
        (
            '#0020080314V#010F这里就是浴室呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080315V先把行李放到房间里，\n',
            '然后再来泡澡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_08E1')
    def lambda_08E1():
        ChrTurnDirection(0x0107, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_08E1)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080316V#001F嗯，好啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_97C')

    def _loc_90F(): pass

    label('loc_90F')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_925',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_92C')

    def _loc_925(): pass

    label('loc_925')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_92C(): pass

    label('loc_92C')

    ChrTalk(
        0x0102,
        (
            '#0020080317V#010F这里就是浴室呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080318V先把行李放到房间里，\n',
            '然后再来泡澡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_97C(): pass

    label('loc_97C')

    Jump('loc_A30')

    def _loc_97F(): pass

    label('loc_97F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 3, 0x523)),
            Expr.Return,
        ),
        'loc_9DC',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '女浴室\n',
            '　需要使用的时候\n',
            '　请通知前台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_A30')

    def _loc_9DC(): pass

    label('loc_9DC')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上贴着一张纸条。\n',
            '『打扫中，停止使用』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_A30(): pass

    label('loc_A30')

    TalkEnd(0x00FF)

    Return()

# id: 0x000F offset: 0xA34
@scena.Code('func_0F_A34')
def func_0F_A34():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A5, 0, 0x528)),
            Expr.Return,
        ),
        'loc_A45',
    )

    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    Call(0, 0x0010)

    Jump('loc_C6C')

    def _loc_A45(): pass

    label('loc_A45')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 5, 0x525)),
            Expr.Return,
        ),
        'loc_BBB',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '男浴室\n',
            '　需要使用的时候\n',
            '　请通知前台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_B4B',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AC0',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_AC7')

    def _loc_AC0(): pass

    label('loc_AC0')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_AC7(): pass

    label('loc_AC7')

    ChrTalk(
        0x0102,
        (
            '#0020080319V#010F这里就是浴室呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080320V先把行李放到房间里，\n',
            '然后再来泡澡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0B1D')
    def lambda_0B1D():
        ChrTurnDirection(0x0107, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0B1D)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010080321V#001F嗯，好啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BB8')

    def _loc_B4B(): pass

    label('loc_B4B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B61',
    )

    ChrTurnDirection(0x0102, 0x0001, 400)

    Jump('loc_B68')

    def _loc_B61(): pass

    label('loc_B61')

    ChrTurnDirection(0x0102, 0x0000, 400)

    def _loc_B68(): pass

    label('loc_B68')

    ChrTalk(
        0x0102,
        (
            '#0020080322V#010F这里就是浴室呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020080323V先把行李放到房间里，\n',
            '然后再来泡澡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_BB8(): pass

    label('loc_BB8')

    Jump('loc_C6C')

    def _loc_BBB(): pass

    label('loc_BBB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A4, 3, 0x523)),
            Expr.Return,
        ),
        'loc_C18',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '男浴室\n',
            '　需要使用的时候\n',
            '　请通知前台。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    Jump('loc_C6C')

    def _loc_C18(): pass

    label('loc_C18')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上贴着一张纸条。\n',
            '『打扫中，停止使用』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)

    def _loc_C6C(): pass

    label('loc_C6C')

    TalkEnd(0x00FF)

    Return()

# id: 0x0010 offset: 0xC70
@scena.Code('func_10_C70')
def func_10_C70():
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
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
        10,
        10,
        1,
        (
            TXT(0x00, '入浴\n'),
            TXT(0x01, '离开\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_CCB'),
        (0x00000001, 'loc_EF5'),
        (-1, 'loc_EF8'),
    )

    def _loc_CCB(): pass

    label('loc_CCB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_CE8',
    )

    OP_6F(0x0009, 0)
    OP_70(0x0009, 29)
    Sleep(200)

    Jump('loc_CFB')

    def _loc_CE8(): pass

    label('loc_CE8')

    OP_6F(0x0008, 0)
    OP_70(0x0008, 29)
    Sleep(200)

    def _loc_CFB(): pass

    label('loc_CFB')

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0008, 0)
    OP_6F(0x0009, 0)
    Sleep(600)

    PlaySE(162, 0x00, 0x64)
    Sleep(1500)

    PlaySE(11, 0x00, 0x64)
    Sleep(800)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 4, 0xC)),
            Expr.Return,
        ),
        'loc_DBF',
    )

    SetChrPos(0x0000, -1000, 0, -5090, 90)
    SetChrPos(0x0001, -1000, 0, -5090, 90)
    SetChrPos(0x0002, -1000, 0, -5090, 90)
    SetChrPos(0x0003, -1000, 0, -5090, 90)
    SetChrPos(0x0004, -1000, 0, -5090, 90)
    SetChrPos(0x0005, -1000, 0, -5090, 90)
    SetChrPos(0x0006, -1000, 0, -5090, 90)
    SetChrPos(0x0007, -1000, 0, -5090, 90)

    Jump('loc_E47')

    def _loc_DBF(): pass

    label('loc_DBF')

    SetChrPos(0x0000, -1000, 0, 4900, 90)
    SetChrPos(0x0001, -1000, 0, 4900, 90)
    SetChrPos(0x0002, -1000, 0, 4900, 90)
    SetChrPos(0x0003, -1000, 0, 4900, 90)
    SetChrPos(0x0004, -1000, 0, 4900, 90)
    SetChrPos(0x0005, -1000, 0, 4900, 90)
    SetChrPos(0x0006, -1000, 0, 4900, 90)
    SetChrPos(0x0007, -1000, 0, 4900, 90)

    def _loc_E47(): pass

    label('loc_E47')

    If(
        (
            (Expr.Eval, "OP_42(0x0000)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E5A',
    )

    SetChrStatus(0x0000, 0xFB, 0)

    def _loc_E5A(): pass

    label('loc_E5A')

    If(
        (
            (Expr.Eval, "OP_42(0x0001)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E6D',
    )

    SetChrStatus(0x0001, 0xFB, 0)

    def _loc_E6D(): pass

    label('loc_E6D')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E80',
    )

    SetChrStatus(0x0002, 0xFB, 0)

    def _loc_E80(): pass

    label('loc_E80')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E93',
    )

    SetChrStatus(0x0003, 0xFB, 0)

    def _loc_E93(): pass

    label('loc_E93')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EA6',
    )

    SetChrStatus(0x0005, 0xFB, 0)

    def _loc_EA6(): pass

    label('loc_EA6')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EB9',
    )

    SetChrStatus(0x0004, 0xFB, 0)

    def _loc_EB9(): pass

    label('loc_EB9')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ECC',
    )

    SetChrStatus(0x0006, 0xFB, 0)

    def _loc_ECC(): pass

    label('loc_ECC')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_EDF',
    )

    SetChrStatus(0x0007, 0xFB, 0)

    def _loc_EDF(): pass

    label('loc_EDF')

    OP_69(0x0000, 0)
    OP_30(0x00)
    FadeIn(1000, 0)
    OP_0D()

    Jump('loc_EFB')

    def _loc_EF5(): pass

    label('loc_EF5')

    Jump('loc_EFB')

    def _loc_EF8(): pass

    label('loc_EF8')

    Jump('loc_EFB')

    def _loc_EFB(): pass

    label('loc_EFB')

    ClearScenaFlags(ScenaFlag(0x0001, 4, 0xC))
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
