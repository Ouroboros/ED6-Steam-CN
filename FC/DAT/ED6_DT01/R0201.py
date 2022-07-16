import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R0201_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R0201   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '魔兽'),
    TXT(0x02, '魔兽'),
    TXT(0x03, '魔兽'),
    TXT(0x04, '魔兽'),
    TXT(0x05, '艾丝蒂尔'),
    TXT(0x06, '约修亚'),
    TXT(0x07, '艾丝蒂尔'),
    TXT(0x08, '约修亚'),
    TXT(0x09, '洛连特方向'),
    TXT(0x0A, '威尔特桥·关所方向'),
    TXT(0x0B, '帕赛尔农场方向'),
    TXT(0x0C, '跳跳猫'),
    TXT(0x0D, '爆种铃兰'),
    TXT(0x0E, '红茶钳虫'),
    TXT(0x0F, '跳跳猫'),
    TXT(0x10, '爆种铃兰'),
    TXT(0x11, '红茶钳虫'),
    TXT(0x12, '跳跳猫'),
    TXT(0x13, '红茶钳虫'),
    TXT(0x14, '爆种铃兰'),
    TXT(0x15, '红茶钳虫'),
    TXT(0x16, '爆种铃兰'),
    TXT(0x17, '爆种铃兰'),
    TXT(0x18, '跳跳猫'),
    TXT(0x19, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'R0201.x'
    header.mapIndex       = 22
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/R0201._SN', 'ED6_DT01/R0201_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xAD4
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
            dword_28        = 3200,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 22,
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
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT07/CH00000._CH', 'ED6_DT07/CH00000P._CP'),
        ('ED6_DT07/CH00010._CH', 'ED6_DT07/CH00010P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT09/CH10020._CH', 'ED6_DT09/CH10020P._CP'),
        ('ED6_DT09/CH10021._CH', 'ED6_DT09/CH10021P._CP'),
        ('ED6_DT09/CH10180._CH', 'ED6_DT09/CH10180P._CP'),
        ('ED6_DT09/CH10181._CH', 'ED6_DT09/CH10181P._CP'),
        ('ED6_DT09/CH10260._CH', 'ED6_DT09/CH10260P._CP'),
        ('ED6_DT09/CH10261._CH', 'ED6_DT09/CH10261P._CP'),
        ('ED6_DT09/CH10210._CH', 'ED6_DT09/CH10210P._CP'),
        ('ED6_DT09/CH10211._CH', 'ED6_DT09/CH10211P._CP'),
        ('ED6_DT07/CH00107._CH', 'ED6_DT07/CH00107P._CP'),
        ('ED6_DT07/CH00001._CH', 'ED6_DT07/CH00001P._CP'),
        ('ED6_DT07/CH00011._CH', 'ED6_DT07/CH00011P._CP'),
    ]

# id: 0x10002 offset: 0x142
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 9,
            chipIndex           = 9,
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
            direction           = 0,
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
            dword_10            = 6,
            chipIndex           = 6,
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
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -131580,
            z                   = 0,
            y                   = -18130,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -224350,
            z                   = 20,
            y                   = -16180,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -184980,
            z                   = 0,
            y                   = -81290,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x2A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -160000,
            z           = 200,
            y           = -2000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -161000,
            z           = 0,
            y           = -21000,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -155000,
            z           = 0,
            y           = -44000,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -178000,
            z           = 500,
            y           = -29000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -190000,
            z           = 0,
            y           = -39000,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -205000,
            z           = 200,
            y           = -55000,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -193000,
            z           = 200,
            y           = -2000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -207000,
            z           = 200,
            y           = -6000,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -198000,
            z           = 300,
            y           = -47000,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -180000,
            z           = -500,
            y           = -58000,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0080,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -159000,
            z           = 200,
            y           = -59000,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0085,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -180000,
            z           = 0,
            y           = -5000,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0085,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -172000,
            z           = 200,
            y           = -43000,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x007B,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x40E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x40E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -204160,
            triggerZ            = 0,
            triggerY            = -21600,
            triggerRange        = 1700,
            actorX              = -204160,
            actorZ              = 2500,
            actorY              = -21600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -179550,
            triggerZ            = 0,
            triggerY            = -15360,
            triggerRange        = 1500,
            actorX              = -179550,
            actorZ              = 1500,
            actorY              = -15360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -176080,
            triggerZ            = 50,
            triggerY            = 11940,
            triggerRange        = 1000,
            actorX              = -176140,
            actorZ              = 1050,
            actorY              = 12680,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -211720,
            triggerZ            = 20,
            triggerY            = -56010,
            triggerRange        = 1000,
            actorX              = -211660,
            actorZ              = 20,
            actorY              = -56570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -145080,
            triggerZ            = 40,
            triggerY            = -50920,
            triggerRange        = 1000,
            actorX              = -144640,
            actorZ              = 40,
            actorY              = -51360,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x4C2
@scena.Code('PreInit')
def PreInit():
    SetChrFlags(0x0008, 0x0040)
    SetChrFlags(0x0009, 0x0040)
    SetChrFlags(0x000A, 0x0040)
    SetChrFlags(0x000B, 0x0040)
    SetChrFlags(0x000C, 0x0040)
    SetChrFlags(0x000D, 0x0040)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000F, 0x0040)

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_4F6'),
        (-1, 'loc_529'),
    )

    def _loc_4F6(): pass

    label('loc_4F6')

    SetChrPos(0x0101, -184970, -500, -80630, 0)
    SetChrPos(0x0102, -184970, -500, -80630, 0)
    SetMapFlags(0x00400000)
    ClearMapFlags(0x00000001)
    Event(0, 0x0003)

    Jump('loc_529')

    def _loc_529(): pass

    label('loc_529')

    Return()

# id: 0x0001 offset: 0x52A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x01, 0x0008)"),
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x40)"),
            Expr.Or,
            Expr.Return,
        ),
        'loc_543',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_55A')

    def _loc_543(): pass

    label('loc_543')

    If(
        (
            (Expr.Eval, "OP_29(0x0006, 0x00, 0x08)"),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_55A',
    )

    OP_64(0x00, 0x0001)

    Jump('loc_55A')

    def _loc_55A(): pass

    label('loc_55A')

    OP_16(0x02, 4000, -306000, -162000, 196620)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0052, 7, 0x297)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_57E',
    )

    OP_6F(0x0000, 0)

    Jump('loc_585')

    def _loc_57E(): pass

    label('loc_57E')

    OP_6F(0x0000, 60)

    def _loc_585(): pass

    label('loc_585')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 0, 0x298)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_597',
    )

    OP_6F(0x0001, 0)

    Jump('loc_59E')

    def _loc_597(): pass

    label('loc_597')

    OP_6F(0x0001, 60)

    def _loc_59E(): pass

    label('loc_59E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 1, 0x299)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B0',
    )

    OP_6F(0x0002, 0)

    Jump('loc_5B7')

    def _loc_5B0(): pass

    label('loc_5B0')

    OP_6F(0x0002, 60)

    def _loc_5B7(): pass

    label('loc_5B7')

    Return()

# id: 0x0002 offset: 0x5B8
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5CD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_5CD(): pass

    label('loc_5CD')

    Return()

# id: 0x0003 offset: 0x5CE
@scena.Code('func_03_5CE')
def func_03_5CE():
    EventBegin(0x00)
    CameraMove(-185000, -500, -66930, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(225000, 0)
    OP_6E(262, 0)
    CreateThread(0x0102, 0x00, 0x00, 0x0004)
    Sleep(800)

    ChrWalkTo(0x0101, -185130, -500, -69810, 3000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#0020001631V#010F我们赶快回协会吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020001632V#010F把这份工作报告做好之后，\n',
            '继续去做下一个任务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010001633V#001F嗯，好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010001634V#001F就这样接着做下去吧～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearMapFlags(0x00400000)
    SetScenaFlags(ScenaFlag(0x0047, 1, 0x239))
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x6D7
@scena.Code('func_04_6D7')
def func_04_6D7():
    ChrWalkTo(0x00FE, -185200, -500, -67940, 3000, 0x00)
    ChrTurnDirection(0x00FE, 0x0101, 400)

    Return()

# id: 0x0005 offset: 0x6F3
@scena.Code('func_05_6F3')
def func_05_6F3():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　帕赛尔农场',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x734
@scena.Code('func_06_734')
def func_06_734():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0052, 7, 0x297)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_81E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_7A8',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0052, 7, 0x297))

    Jump('loc_81B')

    def _loc_7A8(): pass

    label('loc_7A8')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_81B(): pass

    label('loc_81B')

    Jump('loc_856')

    def _loc_81E(): pass

    label('loc_81E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x77)
    def _loc_856(): pass

    label('loc_856')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x864
@scena.Code('func_07_864')
def func_07_864():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 0, 0x298)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_94E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_8D8',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0053, 0, 0x298))

    Jump('loc_94B')

    def _loc_8D8(): pass

    label('loc_8D8')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_94B(): pass

    label('loc_94B')

    Jump('loc_986')

    def _loc_94E(): pass

    label('loc_94E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x78)
    def _loc_986(): pass

    label('loc_986')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0x994
@scena.Code('func_08_994')
def func_08_994():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0053, 1, 0x299)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A7E',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_A08',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0053, 1, 0x299))

    Jump('loc_A7B')

    def _loc_A08(): pass

    label('loc_A08')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_A7B(): pass

    label('loc_A7B')

    Jump('loc_AB4')

    def _loc_A7E(): pass

    label('loc_A7E')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x79)
    def _loc_AB4(): pass

    label('loc_AB4')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
