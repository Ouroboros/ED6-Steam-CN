import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0311_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0311   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '提妲'),
    TXT(0x02, '科洛丝'),
    TXT(0x03, '雪拉扎德'),
    TXT(0x04, 'tarotto'),
    TXT(0x05, 'tarotto'),
    TXT(0x06, 'tarotto'),
    TXT(0x07, 'tarotto'),
    TXT(0x08, 'tarotto'),
    TXT(0x09, 'tarotto'),
    TXT(0x0A, '酒杯'),
    TXT(0x0B, '照片'),
    TXT(0x0C, '莱娜'),
    TXT(0x0D, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0311.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2F7E
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
        ('ED6_DT26/CH20230._CH', 'ED6_DT26/CH20230P._CP'),
        ('ED6_DT26/CH20226._CH', 'ED6_DT26/CH20226P._CP'),
        ('ED6_DT07/CH00023._CH', 'ED6_DT07/CH00023P._CP'),
        ('ED6_DT06/CH20133._CH', 'ED6_DT06/CH20133P._CP'),
        ('ED6_DT26/CH20328._CH', 'ED6_DT26/CH20328P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT26/CH20338._CH', 'ED6_DT26/CH20338P._CP'),
        ('ED6_DT26/CH20333._CH', 'ED6_DT26/CH20333P._CP'),
        ('ED6_DT26/CH20315._CH', 'ED6_DT26/CH20315P._CP'),
        ('ED6_DT26/CH20278._CH', 'ED6_DT26/CH20278P._CP'),
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
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
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
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589834,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589834,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589834,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589834,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589834,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 589834,
            chipIndex           = 10,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 327686,
            chipIndex           = 6,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 786438,
            chipIndex           = 6,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x282
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x282
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 250,
            y           = 0,
            z           = -4510,
            range       = 1700,
            dword_10    = 0x000007D0,
            dword_14    = 0x000002BC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x2A2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 146350,
            triggerZ            = 0,
            triggerY            = 144640,
            triggerRange        = 800,
            actorX              = 147980,
            actorZ              = 1200,
            actorY              = 145500,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 72740,
            triggerZ            = 0,
            triggerY            = 71390,
            triggerRange        = 800,
            actorX              = 73030,
            actorZ              = 1200,
            actorY              = 72380,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 8470,
            triggerZ            = 0,
            triggerY            = 67050,
            triggerRange        = 1200,
            actorX              = 8470,
            actorZ              = 500,
            actorY              = 67050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 9830,
            triggerZ            = 0,
            triggerY            = 70700,
            triggerRange        = 800,
            actorX              = 9830,
            actorZ              = 800,
            actorY              = 70700,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x332
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_343',
    )

    OP_A3(0x10F0)
    Event(0, 0x0002)

    Jump('loc_35A')

    def _loc_343(): pass

    label('loc_343')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_35A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x75),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F1)
    Event(0, 0x0008)

    def _loc_35A(): pass

    label('loc_35A')

    Return()

# id: 0x0001 offset: 0x35B
@scena.Code('Init')
def Init():
    OP_78(0x8C, 0x8C, 0xB4)
    OP_82(0x80, 0x00)
    OP_82(0x81, 0x00)
    OP_79(0x00, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_79(0x05, 0x0002)
    OP_79(0x06, 0x0002)
    OP_79(0x07, 0x0002)
    OP_79(0x08, 0x0002)
    OP_79(0x09, 0x0002)
    OP_79(0x0A, 0x0002)
    OP_79(0x0B, 0x0002)
    OP_79(0x0C, 0x0002)
    OP_79(0x0D, 0x0002)
    OP_79(0x0E, 0x0002)
    OP_79(0x0F, 0x0002)
    OP_79(0x10, 0x0002)
    OP_79(0x11, 0x0002)
    OP_79(0x12, 0x0002)
    OP_79(0x13, 0x0002)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 7, 0x1817)),
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 0, 0x1828)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_49E',
    )

    SetChrFlags(0x0008, 0x0002)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0040)
    SetChrPos(0x0008, 148300, 400, 144950, 180)
    SetChrChipByIndex(0x0008, 1)
    SetChrSubChip(0x0008, 0)
    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0002)
    SetChrFlags(0x0009, 0x0004)
    SetChrFlags(0x0009, 0x0040)
    SetChrPos(0x0009, 72990, 450, 72950, 270)
    SetChrChipByIndex(0x0009, 2)
    SetChrSubChip(0x0009, 0)
    ClearChrFlags(0x0009, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 1, 0x1819)),
            Expr.Return,
        ),
        'loc_433',
    )

    OP_6F(0x0006, 10)
    OP_70(0x0006, 0x0000000A)

    Jump('loc_441')

    def _loc_433(): pass

    label('loc_433')

    OP_6F(0x0006, 15)
    OP_70(0x0006, 0x0000000F)

    def _loc_441(): pass

    label('loc_441')

    OP_72(0x0002, 0x0010)
    OP_71(0x0007, 0x0000)
    OP_71(0x0007, 0x0004)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_72(0x0007, 0x0020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 2, 0x181A)),
            Expr.Return,
        ),
        'loc_477',
    )

    OP_6F(0x0000, 12)
    OP_70(0x0000, 0x0000000C)

    Jump('loc_49E')

    def _loc_477(): pass

    label('loc_477')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 0, 0x1818)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_490',
    )

    OP_6F(0x0000, 12)
    OP_70(0x0000, 0x0000000C)

    Jump('loc_49E')

    def _loc_490(): pass

    label('loc_490')

    OP_6F(0x0000, 50)
    OP_70(0x0000, 0x00000032)

    def _loc_49E(): pass

    label('loc_49E')

    Return()

# id: 0x0002 offset: 0x49F
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_6D(144440, 0, 145300, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_BB(0x00, 0x01, 0x00000043)
    OP_BD()
    SetChrFlags(0x0101, 0x0002)
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0101, 0x0040)
    SetChrFlags(0x0008, 0x0002)
    SetChrFlags(0x0008, 0x0004)
    SetChrFlags(0x0008, 0x0040)
    SetChrChipByIndex(0x0101, 0)
    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0008, 1)
    SetChrSubChip(0x0008, 0)
    SetChrPos(0x0008, 148300, 400, 144950, 180)
    SetChrPos(0x0101, 147700, 450, 145270, 180)
    ClearChrFlags(0x0008, 0x0080)
    OP_71(0x0007, 0x0000)
    OP_71(0x0007, 0x0004)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_6F(0x0000, 11)
    OP_70(0x0000, 0x0000000B)
    Sleep(500)

    FadeIn(1000, 0)
    OP_6D(148090, 0, 145410, 2500)
    OP_0D()
    OP_22(0x0007, 0x00, 0x46)
    Sleep(1000)

    OP_62(0x0101, 0xFFFFFDDA, 1200, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_6F(0x0000, 11)
    OP_70(0x0000, 0x00000014)
    OP_99(0x0101, 0x00, 0x07, 0x00000320)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010290132V#1340F#5P………啊……………',
            TxtCtl.Enter,
        ),
    )

    SetChrSubChip(0x0101, 17)
    CloseMessageWindow()
    SetChrSubChip(0x0101, 20)
    Sleep(500)

    SetChrSubChip(0x0101, 23)
    Sleep(500)

    SetChrSubChip(0x0101, 20)
    Sleep(500)

    SetChrSubChip(0x0101, 23)
    OP_99(0x0101, 0x12, 0x13, 0x00000320)
    SetChrSubChip(0x0101, 17)

    ChrTalk(
        0x0101,
        (
            '#0010290133V#1335F刚才是……门的声音吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290134V#451F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    ClearChrFlags(0x0101, 0x0002)
    ClearChrFlags(0x0101, 0x0004)
    SetChrChipByIndex(0x0101, 65535)
    SetChrSubChip(0x0101, 0)
    SetChrPos(0x0101, 146350, 0, 144660, 270)
    OP_6D(146930, 0, 144820, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0070290135V#40W……嗯…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6F(0x0000, 20)
    OP_70(0x0000, 0x00000032)
    OP_99(0x0008, 0x00, 0x09, 0x00000258)
    OP_8C(0x0101, 90, 400)
    SetChrSubChip(0x0008, 10)
    Sleep(300)

    ChrTalk(
        0x0008,
        (
            '#0070290136V#1252F#40W……啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290137V姐姐……\n',
            '……怎么了……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290138V#1336F#6P抱歉，吵醒你了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290139V#1333F我担心门是不是关好了，\n',
            '去确认一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290140V马上回来，你睡吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0070290141V#1250F#40W……嗯……知道了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290142V#1251F姐姐……\n',
            '……早点回来哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x0B, 0x13, 0x00000320)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290143V#1336F#6P嘿嘿……真可爱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290144V#1331F嗯～突然心血来潮\n',
            '想戳戳她脸蛋了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290145V#455F……喔，不行不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetChrFlags(0x0101, 0x0004)
    OP_8F(0x0101, 146680, 0, 144810, 500, 0x00)
    Sleep(500)

    OP_6F(0x0000, 50)
    OP_70(0x0000, 0x0000000C)
    OP_73(0x0000)
    Sleep(1000)

    OP_8F(0x0101, 146350, 0, 144660, 500, 0x00)
    ClearChrFlags(0x0101, 0x0004)
    Sleep(500)

    OP_8C(0x0101, 180, 400)
    Sleep(500)

    ClearChrFlags(0x0101, 0x0040)

    ChrTalk(
        0x0101,
        (
            '#0010290146V#1335F#5P（虽然可能是雪拉姐\n',
            '  或者科洛丝……)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290147V（不过还是去确认一下门关没关好吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1817)
    OP_28(0x0090, 0x01, 0x0400)
    SetChrStatus(ChrTable['艾丝蒂尔'], 0xFE, 0)
    SetChrStatus(ChrTable['约修亚'], 0xFE, 0)
    SetChrStatus(ChrTable['雪拉扎德'], 0xFE, 0)
    SetChrStatus(ChrTable['提妲'], 0xFE, 0)
    SetChrStatus(ChrTable['科洛丝'], 0xFE, 0)
    SetChrStatus(ChrTable['阿加特'], 0xFE, 0)
    SetChrStatus(ChrTable['金'], 0xFE, 0)
    SetChrStatus(ChrTable['奥利维尔'], 0xFE, 0)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0xA1B
@scena.Code('func_03_A1B')
def func_03_A1B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 1, 0x1819)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_CEE',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(72560, 0, 72180, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 72610, 0, 71390, 360)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0060290148V#1240F#40W呼……呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290149V#457F睡得好香……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290150V#1336F呵呵、科洛丝啊，\n',
            '把她带到约修亚的房间的时候\n',
            '还手忙脚乱了呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290151V真可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0060290152V#1241F#40W……嗯………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x00, 0x05, 0x000005DC)
    Sleep(300)

    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0009,
        (
            '#0060290153V#1241F#40W……老师……大家……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290154V#40W……我………\n',
            '………怎么办…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290155V#40W……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290148V#1240F#40W呼……呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290157V#1339F科洛丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetChrFlags(0x0101, 0x0004)
    OP_8F(0x0101, 72640, 0, 71580, 500, 0x00)
    Sleep(500)

    OP_B0(0x0006, 0x0F)
    OP_6F(0x0006, 15)
    OP_70(0x0006, 0x0000000A)
    OP_99(0x0009, 0x05, 0x07, 0x000003E8)
    OP_73(0x0006)
    Sleep(1000)

    OP_8F(0x0101, 72610, 0, 71390, 500, 0x00)
    ClearChrFlags(0x0101, 0x0004)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290158V#1337F……我们俩都要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x1819)
    EventEnd(0x00)

    Jump('loc_D3A')

    def _loc_CEE(): pass

    label('loc_CEE')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '科洛丝以平静的表情熟睡着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_D3A(): pass

    label('loc_D3A')

    Return()

# id: 0x0004 offset: 0xD3B
@scena.Code('func_04_D3B')
def func_04_D3B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 0, 0x1818)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_D90',
    )

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲以平静的表情熟睡着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Jump('loc_1027')

    def _loc_D90(): pass

    label('loc_D90')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 2, 0x181A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FDD',
    )

    EventBegin(0x00)
    Fade(1000)
    OP_6D(147270, 0, 145070, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0101, 146350, 0, 144680, 90)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0070290159V#1253F#40W……呜……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290160V#40W爸爸……妈妈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0070290161V#1253F#40W我……\n',
            '会好好听话……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290162V#40W姐姐她们\n',
            '也在一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290163V#40W……所以……放心吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290164V#40W……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290165V#1251F#40W嘿嘿……呜喵呜喵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290166V#1339F#6P提妲……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    SetChrFlags(0x0101, 0x0004)
    OP_8F(0x0101, 146680, 0, 144810, 500, 0x00)
    Sleep(500)

    OP_6F(0x0000, 50)
    OP_70(0x0000, 0x0000000C)
    OP_73(0x0000)
    Sleep(1000)

    OP_8F(0x0101, 146350, 0, 144680, 500, 0x00)
    ClearChrFlags(0x0101, 0x0004)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290167V#1342F#6P没关系……\n',
            '有我们在。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x181A)
    EventEnd(0x00)

    Jump('loc_1027')

    def _loc_FDD(): pass

    label('loc_FDD')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '提妲以平静的表情熟睡着。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_1027(): pass

    label('loc_1027')

    Return()

# id: 0x0005 offset: 0x1028
@scena.Code('func_05_1028')
def func_05_1028():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 3, 0x181B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10C9',
    )

    OP_8C(0x0101, 180, 0)

    ChrTalk(
        0x0101,
        (
            '#0010290171V#453F啊……',
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
            '床还是温热的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010290172V#1335F雪拉姐……\n',
            '去哪儿了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x181B)
    TalkEnd(0x00FF)

    Jump('loc_1109')

    def _loc_10C9(): pass

    label('loc_10C9')

    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '床还是温热的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    def _loc_1109(): pass

    label('loc_1109')

    Return()

# id: 0x0006 offset: 0x110A
@scena.Code('func_06_110A')
def func_06_110A():
    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    OP_22(0x0074, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x1152
@scena.Code('func_07_1152')
def func_07_1152():
    EventBegin(0x00)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, -8070, 200, 2290, 180)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0011, -7800, 700, 1240, 0)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x000C, -8140, 730, 1400, 0)
    SetChrPos(0x000D, -8640, 730, 1400, 0)
    SetChrPos(0x000F, -8140, 730, 940, 0)
    SetChrPos(0x0010, -8640, 730, 940, 0)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ChrTurnDirection(0x0101, 0x0103, 0)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    OP_6D(-8070, 0, 2290, 3000)

    ChrTalk(
        0x000A,
        (
            '#0030290173V#026F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0101, 820, 0, -2480, 300)

    ChrTalk(
        0x0101,
        (
            '#0010290174V#3P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 1700, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    @scena.Lambda('lambda_128B')
    def lambda_128B():
        OP_8E(0x00FE, -5040, 0, -280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_128B)

    @scena.Lambda('lambda_12A6')
    def lambda_12A6():
        OP_6D(-6710, 0, 880, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12A6)

    SetChrSubChip(0x000A, 1)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0030290175V#023F呀……\n',
            '艾丝蒂尔，怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290176V#454F嗯，听到点声音\n',
            '就醒来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290177V是雪拉姐啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290178V#020F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290179V#021F呵呵，感觉到气息就醒来～\n',
            '挺像正游击士的样子了嘛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290180V#1331F嘿嘿……\n',
            '可能有点紧张了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290181V#1336F似乎发生了很多事\n',
            '脑子有点混乱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030281672V#524F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1428')
    def lambda_1428():
        OP_8E(0x00FE, -7470, 0, -430, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1428)

    @scena.Lambda('lambda_1443')
    def lambda_1443():
        OP_6D(-7650, 0, 970, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1443)

    Sleep(500)

    SetChrSubChip(0x000A, 0)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_146F')
    def lambda_146F():
        OP_96(0x00FE, 0xFFFFDFEE, 0x000000C8, 0xFFFFFDBC, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_146F)

    OP_8C(0x0101, 0, 1000)
    WaitForThreadExit(0x0101, 0x0001)
    SetChrChipByIndex(0x0101, 5)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290183V#1333F#6P雪拉姐，在看什么啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290184V#027F#5P这个啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_14F6')
    def lambda_14F6():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000000C8)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_14F6)

    SetChrFlags(0x000A, 0x0002)
    SetChrChipByIndex(0x000A, 4)
    OP_99(0x000A, 0x08, 0x0A, 0x00000190)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0030290185V#026F#5P逆位的皇帝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290186V慈悲，共鸣，信任，障碍，不成熟。\n',
            '──还有对敌人的困惑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290187V#1335F#6P感、感觉上，\n',
            '真是张故弄玄虚的卡牌啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290188V#455F对敌人的困惑，\n',
            '稍微有点不理解……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000C, 10)
    SetChrSubChip(0x000C, 12)

    @scena.Lambda('lambda_1609')
    def lambda_1609():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x000000C8)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_1609)

    ClearChrFlags(0x000A, 0x0002)
    SetChrSubChip(0x000A, 0)
    SetChrChipByIndex(0x000A, 3)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0030290189V#026F#5P呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290190V#524F今天不是\n',
            '给艾丝蒂尔占卜的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290191V#453F#6P啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290192V#020F#5P呵呵，你似乎\n',
            '也有心事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290193V那个记者的事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290194V#1340F#6P啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290195V#452F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290196V#524F#5P并不是在逼你。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290197V只是，心情整理好之后\n',
            '说出来也好哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290198V#452F#6P…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290199V#1340F雪拉姐……\n',
            '能听我倾诉吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290200V#027F#5P你就是我妹妹。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290201V姐姐这身份\n',
            '就是这时候用的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290202V#1339F#6P雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290203V#452F……这个，能看看吗？',
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
            '把朵洛希的照片递给雪拉扎德。',
            (TxtCtl.SetColor, 0x0),
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
            '#0030290204V#023F#5P照片……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x000A, 0x0002)
    SetChrChipByIndex(0x000A, 4)
    SetChrSubChip(0x000A, 9)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0030290205V#023F#5P…………………………\n',
            '…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290206V#026F……原来如此啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290207V#524F这个，就是\n',
            '你消沉的原因啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290208V#455F#6P……嗯………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290209V#027F#5P应该是为隐秘活动\n',
            '而准备的藏身之地……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290210V没错，要是他还身为游击士\n',
            '就不能用这方法了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290211V那……目标是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290212V#1335F#6P雪拉姐……你不惊讶吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x000A, 0x0002)
    SetChrSubChip(0x000A, 0)
    SetChrChipByIndex(0x000A, 3)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0030290213V#026F#5P说实话，我还以为\n',
            '他在做更严重的事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290214V#524F但是、空贼艇的抢夺事件\n',
            '只是把士兵打晕了而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290215V的确很像是约修亚\n',
            '会做得事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290216V#1339F#6P是，是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290217V#025F#5P不过，被拍到照片\n',
            '就有点大意了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290218V不像他呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290219V#1336F#6P这个嘛……\n',
            '因为这是朵洛希拍的照片嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290220V一扯上照相机，\n',
            '她可是有天才的运气和实力嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290221V#027F#5P原来如此，那个戴眼镜的女孩啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290222V#452F#6P……对了，雪拉姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290223V这个照片……\n',
            '是不是应该交给协会？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290224V#026F#5P身为一个游击士，\n',
            '被赋予的义务只有一个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290225V#020F就是拯救被恶人伤害的\n',
            '民间人士而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290226V你觉得约修亚和空贼混在一起\n',
            '是想伤害民间人士吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290227V#1330F#6P那、那种事\n',
            '约修亚不可能会做的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290228V#027F#5P那就没有特地\n',
            '报告的义务了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290229V我也不打算\n',
            '特地去报告这事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290230V说到底，你只要\n',
            '相信约修亚就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290231V#452F#6P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290232V#524F#5P还是说……你不相信他？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290233V#452F#6P相信……虽然相信……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290234V#455F但是……很不安……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290235V他在我不知道的地方，\n',
            '带着那冰冷的眼神……做些胡来的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290236V看起来就像\n',
            '对自己的事漠不关心一样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290237V#1341F干脆和爸爸商量\n',
            '想办法找到他好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290238V#023F#5P……艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290239V#1340F#6P但是，那我\n',
            '是为什么到这里来的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290240V不就是为了亲手\n',
            '把约修亚带回来吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290241V#455F……想到这里\n',
            '脑子就混乱了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290242V#026F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290243V#524F不过啊，艾丝蒂尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290244V你就算不这么焦急，\n',
            '一样也会找到答案的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290245V#1340F#6P……啊………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290246V#020F#5P现在的你，应该能够\n',
            '把握好自己的心情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290247V你只是迷失了\n',
            '自己想做的事而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290248V不要着急，在自己心中\n',
            '一定能找到答案的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290249V#1339F#6P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290250V#027F#5P和下船之后相比\n',
            '似乎镇定多了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290251V至少，现在应该做的事\n',
            '你不是看得很清楚吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290252V#1336F#6P嗯，嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290253V#454F知道鲁克和伊莉莎的妈妈\n',
            '倒下的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290254V知道沮丧也没用，\n',
            '反而有了干劲。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290255V然后，焦躁的心情\n',
            '也减弱了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290256V#1335F我……还是太单纯了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290257V#027F#5P呵呵，没这回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290258V只是，你似乎不习惯\n',
            '停下来的生活。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290259V你是那种不断向前进\n',
            '就会找到答案的类型。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290260V#455F#6P呜呜……好像被捉弄了一样\n',
            '真是高兴不起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290261V#1337F不过，谢谢雪拉姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290262V总觉得……\n',
            '好像能够找到答案了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290263V#027F#5P呵呵……\n',
            '没什么大不了的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290264V#021F话说回来……\n',
            '约修亚也挺有一手的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290265V搞不好和那个空贼小姑娘\n',
            '正打得火热呢㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290266V#455F#6P怎、怎么说到那去了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290267V#459F还、还不确定\n',
            '是那种关系啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290268V#027F#5P哎呀，是吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290269V我记得她是个有点逞强、\n',
            '满男孩子气的女生吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290270V而且，也觉得\n',
            '品性不错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290271V#021F说不定是个不错的发展㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290272V#459F#6P真是的，雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290273V#027F#5P同生死共患难之间\n',
            '萌生了爱情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290274V#023F啊，不过艾丝蒂尔。\n',
            '你不用担心哦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290275V#021F就算约修亚被抢走了，\n',
            '你只要夺回来就行了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290276V#1338F#6P……下次打死我\n',
            '也不找雪拉姐商量了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290277V#021F#5P呵呵，开玩笑啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290278V#526F好了，关于约修亚的烦恼，\n',
            '往这方面想就比较好了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290279V这才比较像个年轻女孩子哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290280V#455F#6P可是这方面\n',
            '其实也很复杂……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290281V#1334F……就算不是这样～\n',
            '还有科洛丝呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290282V#023F#5P啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290283V#1336F#6P没、没什么的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290284V#1331F似乎不知不觉的就镇定下来了。\n',
            '我这就去睡了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290285V雪拉姐还不睡吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290286V#524F#5P不，我也去睡了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290287V难得阿加特他们\n',
            '这么费心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290288V#453F#6P这么说来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290289V#1340F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290290V#020F#5P什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290291V#1335F#6P……倒是雪拉姐\n',
            '是不是有什么烦恼？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290292V#026F#5P算是吧……\n',
            '是有烦恼。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290293V#020F不过、２、３天内\n',
            '应该就会告诉大家了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290294V#455F#6P是吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290295V#454F嗯，那我\n',
            '就不作多余的担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290296V不过……\n',
            '千万别逞强哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290297V#021F#5P呵呵，不必担心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290298V#027F还要照顾\n',
            '身边的妹妹才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290299V#455F#6P真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290300V#1337F算啦。\n',
            '晚安，雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0030290301V#021F#5P晚安，艾丝蒂尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2B71')
    def lambda_2B71():
        OP_96(0x00FE, 0xFFFFE2BE, 0x00000000, 0xFFFFFD94, 0x000001F4, 0x00000FA0)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B71)

    SetChrSubChip(0x0101, 0)
    SetChrChipByIndex(0x0101, 65535)
    OP_8C(0x0101, 90, 1000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    SetChrSubChip(0x000A, 1)

    @scena.Lambda('lambda_2BAF')
    def lambda_2BAF():
        OP_8E(0x0101, 2990, 0, -2590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2BAF)

    @scena.Lambda('lambda_2BCA')
    def lambda_2BCA():
        OP_6D(-5170, 0, -30, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2BCA)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_2BE7')
    def lambda_2BE7():
        OP_6D(-7600, 0, 2870, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2BE7)

    @scena.Lambda('lambda_2BFF')
    def lambda_2BFF():
        OP_6E(245, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2BFF)

    Sleep(1000)

    SetChrSubChip(0x000A, 0)
    WaitForThreadExit(0x0101, 0x0003)

    @scena.Lambda('lambda_2C1E')
    def lambda_2C1E():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0x00, 0x000000C8)

        ExitThread()

    DispatchAsync(0x000D, 0x0002, lambda_2C1E)

    SetChrFlags(0x000A, 0x0002)
    SetChrChipByIndex(0x000A, 4)
    OP_99(0x000A, 0x08, 0x0A, 0x00000190)
    Sleep(500)

    ChrTalk(
        0x000A,
        (
            '#0030290302V#522F#5P逆位的皇帝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290186V慈悲，共鸣，信任，障碍，不成熟。\n',
            '──还有对敌人的困惑。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrSubChip(0x000A, 11)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '#0030290304V#026F#5P只是迷失了\n',
            '该做的事，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290305V#524F呵呵……会是谁呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_20(0x00001770)
    OP_0D()
    Sleep(3000)

    OP_22(0x0118, 0x00, 0x28)
    Sleep(3000)

    OP_21()
    OP_A2(0x10F1)
    NewScene('ED6_DT21/T0300._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2D40
@scena.Code('func_08_2D40')
def func_08_2D40():
    EventBegin(0x00)
    OP_DB()
    SetChrFlags(0x0101, 0x0004)
    SetChrFlags(0x0101, 0x0002)
    SetChrPos(0x0101, 147700, 350, 145310, 320)
    SetChrChipByIndex(0x0101, 7)
    SetChrSubChip(0x0101, 0)
    SetChrFlags(0x0013, 0x0040)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0013, 0x0002)
    SetChrPos(0x0013, 147960, 100, 145220, 320)
    SetChrChipByIndex(0x0013, 8)
    SetChrSubChip(0x0013, 8)
    ClearChrFlags(0x0013, 0x0080)
    OP_6D(145670, 400, 145530, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_71(0x0007, 0x0000)
    OP_71(0x0007, 0x0004)
    OP_72(0x0000, 0x0004)
    OP_72(0x0000, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_6F(0x0000, 15)
    OP_70(0x0000, 0x0000000F)
    FadeIn(1000, 0)
    OP_6D(148490, 400, 145420, 4000)
    OP_62(0x0101, 0xFFFFFED4, 1300, 0x1C, 0x21, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x0101)
    Sleep(1000)

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0013,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    Sleep(1000)

    OP_DC()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0010291029V而夜晚，在母亲温暖的\n',
            '怀抱中入睡……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    FadeOut(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0101, 0x0004)
    SetChrChipByIndex(0x0101, 65535)
    Sleep(500)

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0010291030V没有悲伤，\n',
            '充满温柔的每一天……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0010291031V那确实──\n',
            '是令人满足的时光。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetMapFlags(0x02000000)
    OP_A2(0x10F4)
    NewScene('ED6_DT21/T0300._SN', 101, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
