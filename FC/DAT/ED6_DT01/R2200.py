import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2200   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '克拉姆'),
    TXT(0x02, '玛诺利亚村方向'),
    TXT(0x03, '玛西亚孤儿院方向'),
    TXT(0x04, '卢安方向'),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2200.x'
    header.mapIndex       = 101
    header.bgm            = 20
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1AEA
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
            word_3A         = 101,
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
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP'),
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
        ('ED6_DT09/CH10460._CH', 'ED6_DT09/CH10460P._CP'),
        ('ED6_DT09/CH10461._CH', 'ED6_DT09/CH10461P._CP'),
        ('ED6_DT09/CH10480._CH', 'ED6_DT09/CH10480P._CP'),
        ('ED6_DT09/CH10481._CH', 'ED6_DT09/CH10481P._CP'),
        ('ED6_DT09/CH10470._CH', 'ED6_DT09/CH10470P._CP'),
        ('ED6_DT09/CH10471._CH', 'ED6_DT09/CH10471P._CP'),
    ]

# id: 0x10002 offset: 0x122
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -139370,
            z                   = -2020,
            y                   = 15120,
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
            x                   = -28630,
            z                   = -1990,
            y                   = 79340,
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
            x                   = 7410,
            z                   = -2000,
            y                   = 29980,
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

# id: 0x10003 offset: 0x1A2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -96260,
            z           = -1950,
            y           = 27960,
            word_0C     = 0x00B4,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0181,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -104740,
            z           = -5970,
            y           = 11000,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -81100,
            z           = -5870,
            y           = 13330,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -88220,
            z           = -5960,
            y           = 9810,
            word_0C     = 0x00B4,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x018D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -96260,
            z           = -1950,
            y           = 27960,
            word_0C     = 0x00B4,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0325,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -104740,
            z           = -5970,
            y           = 11000,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0330,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -81100,
            z           = -5870,
            y           = 13330,
            word_0C     = 0x00B4,
            word_0E     = 0x0009,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0330,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -88220,
            z           = -5960,
            y           = 9810,
            word_0C     = 0x00B4,
            word_0E     = 0x000D,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0331,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x282
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -30500,
            y           = 2000,
            z           = 36300,
            range       = -27500,
            dword_10    = 0xFFFFF448,
            dword_14    = 0x00006464,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000002,
        ),
        ScenaEventData(
            x           = -14300,
            y           = 2000,
            z           = 34900,
            range       = -11500,
            dword_10    = 0xFFFFF448,
            dword_14    = 0x000058AC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000004,
        ),
        ScenaEventData(
            x           = -23460,
            y           = 2000,
            z           = 55770,
            range       = -34700,
            dword_10    = 0xFFFFF448,
            dword_14    = 0x0000C760,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -38000,
            y           = 2000,
            z           = 33000,
            range       = -40000,
            dword_10    = 0xFFFFF448,
            dword_14    = 0x000055F0,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
    )

# id: 0x10005 offset: 0x302
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -21830,
            triggerZ            = -2000,
            triggerY            = 37790,
            triggerRange        = 1500,
            actorX              = -21830,
            actorZ              = -800,
            actorY              = 37790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -18840,
            triggerZ            = -2000,
            triggerY            = 33860,
            triggerRange        = 1500,
            actorX              = -18840,
            actorZ              = -500,
            actorY              = 33860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -114230,
            triggerZ            = -6050,
            triggerY            = 11770,
            triggerRange        = 1000,
            actorX              = -114730,
            actorZ              = -6040,
            actorY              = 12270,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -77980,
            triggerZ            = -6870,
            triggerY            = -11780,
            triggerRange        = 1000,
            actorX              = -77540,
            actorZ              = -6730,
            actorY              = -11140,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000A,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x392
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_39E'),
        (-1, 'loc_3B4'),
    )

    def _loc_39E(): pass

    label('loc_39E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B1',
    )

    SetScenaFlags(ScenaFlag(0x0087, 5, 0x43D))
    Event(0, 0x0006)

    def _loc_3B1(): pass

    label('loc_3B1')

    Jump('loc_3B4')

    def _loc_3B4(): pass

    label('loc_3B4')

    Return()

# id: 0x0001 offset: 0x3B5
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3CD',
    )

    OP_B1('R2200_y')

    Jump('loc_3D6')

    def _loc_3CD(): pass

    label('loc_3CD')

    OP_B1('R2200_n')

    def _loc_3D6(): pass

    label('loc_3D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 4, 0x434)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3F9',
    )

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)

    Jump('loc_40D')

    def _loc_3F9(): pass

    label('loc_3F9')

    SetChrFlags(0x0010, 0x0080)
    SetChrFlags(0x0011, 0x0080)
    SetChrFlags(0x0012, 0x0080)
    SetChrFlags(0x0013, 0x0080)

    def _loc_40D(): pass

    label('loc_40D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            Expr.Return,
        ),
        'loc_41D',
    )

    OP_10(0x01, 0x00)
    OP_10(0x03, 0x01)

    Jump('loc_423')

    def _loc_41D(): pass

    label('loc_41D')

    OP_10(0x01, 0x01)
    OP_10(0x03, 0x00)

    def _loc_423(): pass

    label('loc_423')

    OP_16(0x02, 4000, -188000, -109000, 196646)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 1, 0x4B9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_447',
    )

    OP_6F(0x0000, 0)

    Jump('loc_44E')

    def _loc_447(): pass

    label('loc_447')

    OP_6F(0x0000, 60)

    def _loc_44E(): pass

    label('loc_44E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 2, 0x4BA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_460',
    )

    OP_6F(0x0001, 0)

    Jump('loc_467')

    def _loc_460(): pass

    label('loc_460')

    OP_6F(0x0001, 60)

    def _loc_467(): pass

    label('loc_467')

    ExecExpressionWithVar(
        0x2A,
        (
            (Expr.PushLong, 0x186A),
            Expr.Neg,
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(456, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x477
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 6, 0x40E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7F2',
    )

    SetScenaFlags(ScenaFlag(0x0081, 6, 0x40E))
    EventBegin(0x00)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_04A6')
    def lambda_04A6():
        CameraMove(-22740, -1990, 38220, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_04A6)

    @scena.Lambda('lambda_04BE')
    def lambda_04BE():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_04BE)

    @scena.Lambda('lambda_04CE')
    def lambda_04CE():
        CameraSetDistance(2800, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_04CE)

    WaitForThreadExit(0x0000, 0x0002)
    SetChrPos(0x0101, -28320, -2000, 32860, 90)
    SetChrPos(0x0102, -28920, -2000, 32460, 90)

    @scena.Lambda('lambda_0505')
    def lambda_0505():
        ChrWalkTo(0x00FE, -22970, -1990, 37960, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0505)

    Sleep(800)

    @scena.Lambda('lambda_0525')
    def lambda_0525():
        ChrWalkTo(0x00FE, -23310, -2000, 36550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0525)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_0545')
    def lambda_0545():
        SetChrDirection(0x00FE, 90, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0545)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_0558')
    def lambda_0558():
        SetChrDirection(0x00FE, 45, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0558)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　玛西亚孤儿院',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#0010040658V#002F#1P…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_05C5')
    def lambda_05C5():
        CameraMove(-23610, -2000, 39450, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_05C5)

    SetChrDirection(0x0102, 315, 400)
    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020040659V#010F看起来，\n',
            '孤儿院就在这里面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040660V#007F#1P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040661V…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_066C')
    def lambda_066C():
        CameraMove(-22740, -1990, 38220, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_066C)

    ChrTurnDirection(0x0102, 0x0101, 400)
    WaitForThreadExit(0x0000, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020040662V#014F怎么了，艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040663V#006F#1P……好的，我决定了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010040664V#005F#1P就算自己的身世再怎么可怜，\n',
            '偷别人的东西就是不对！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040665V等我抓到那个调皮蛋之后，\n',
            '一定要好好教训教训他！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020040666V#019F哈哈，在烦恼中得出结论，\n',
            '还真是艾丝蒂尔的风格……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040667V#010F不管怎么说，对小孩子还是温柔点好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_7F2(): pass

    label('loc_7F2')

    Return()

# id: 0x0003 offset: 0x7F3
@scena.Code('func_03_7F3')
def func_03_7F3():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 0, 0x410)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1196',
    )

    SetScenaFlags(ScenaFlag(0x0082, 1, 0x411))
    ClearMapFlags(0x00000001)
    EventBegin(0x00)

    ExecExpressionWithValue(
        0x0136,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0136,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0008, 0x0004)
    SetChrPos(0x0008, -22174, -700, 54574, 0)

    NpcTalk(
        0x0008,
        '少年的声音',
        (
            '#0400040862V……科洛丝姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0136, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Fade(1000)
    CameraMove(-25380, -2050, 57450, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -25380, -2000, 57447, 225)
    SetChrPos(0x0136, -26370, -2000, 58130, 180)
    SetChrPos(0x0102, -27810, -2000, 57580, 135)
    OP_0D()
    ChrWalkTo(0x0008, -24790, -700, 52330, 7000, 0x00)
    SetChrDirection(0x0008, 270, 0)
    ChrJumpTo(0x0008, -25650, -2060, 54080, 1000, 7000)
    ChrWalkTo(0x0008, -26900, -2000, 54430, 7000, 0x00)
    SetChrDirection(0x0008, 0, 600)
    ClearChrFlags(0x0008, 0x0004)

    ChrTalk(
        0x0136,
        (
            '#0060040863V#044F克拉姆？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040864V#004F啊，是调皮蛋！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0136, 0x0002)

    ChrTalk(
        0x0136,
        (
            '#0060040865V#042F你呀……\n',
            '怎么到这种地方来玩呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040866V要是碰到魔兽怎么办？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0400040867V#775F我、我只是想和科洛丝姐姐\n',
            '说声对不起而已……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040868V我骗你说没有恶作剧，\n',
            '实在对不起呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040869V#041F呵呵……\n',
            '我并没有生你的气啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040870V#041F不过，\n',
            '你是不是还要向谁道个歉呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0008,
        (
            '#0400040871V#774F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040872V才、才不会呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040873V#000F？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040874V#048F你是个心地很好的孩子，\n',
            '这点我是很清楚的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040875V乖孩子……说声对不起好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0400040876V#773F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040877V既然科洛丝姐姐这样说，\n',
            '那我只有照办了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0BDD')
    def lambda_0BDD():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0BDD')

    DispatchAsync2(0x0101, 0x0001, lambda_0BDD)

    @scena.Lambda('lambda_0BEE')
    def lambda_0BEE():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0BEE')

    DispatchAsync2(0x0136, 0x0001, lambda_0BEE)

    @scena.Lambda('lambda_0BFF')
    def lambda_0BFF():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_0BFF')

    DispatchAsync2(0x0102, 0x0001, lambda_0BFF)

    ChrWalkTo(0x0008, -25435, -2000, 56380, 3000, 0x00)
    ChrTurnDirection(0x0008, 0x0101, 0)

    ChrTalk(
        0x0008,
        (
            '#0400040878V#773F是我不好。\n',
            '游击士姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040879V对……不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040880V#008F啊、啊哈哈……\n',
            '原来你是特意过来向我道歉的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040881V#001F看样子你也有诚实的一面嘛㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrMoveTo(0x0008, -25260, -2100, 55800, 3000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#0400040882V#774F你、你别误会哦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040883V是科洛丝姐姐叫我说，\n',
            '我才这样说的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040884V#772F其实你自己也要检讨一下，\n',
            '做游击士怎么能这么粗心大意呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040885V连像我这样的小孩\n',
            '也能这么容易骗到你，这怎么行？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040886V#009F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpToRelative(0x0008, 0, 0, 0, 800, 6000)

    ChrTalk(
        0x0008,
        (
            '#0400040887V#770F拜拜！\n',
            '要努力锻炼才行哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -24112, -2000, 57350, 6000, 0x00)
    ChrWalkTo(0x0008, -24560, -2000, 74900, 7000, 0x00)
    SetChrFlags(0x0008, 0x0080)

    ChrTalk(
        0x0101,
        (
            '#0010040888V#009F#2P还、还真的是一点都不可爱！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0136, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040889V#010F算啦算啦。\n',
            '他只是害羞而已吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040890V不过那孩子说的倒是很有道理，\n',
            '粗心大意的确是你的缺点。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040891V你不觉得自己还要多锻炼一下才行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040892V#007F#2P哎呀呀……\n',
            '约修亚也越来越不可爱了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0136, 180, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040893V#041F呵呵……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040894V艾丝蒂尔、约修亚，\n',
            '你们两个感情真好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040895V感觉就像真正的姐弟俩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040896V#008F#2P真、真的吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040897V#019F要是从互相照顾的角度来看，\n',
            '倒不如说是兄妹更加贴切吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040898V#009F#2P哼～你不觉得这样说很没礼貌吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040899V#040F呵呵，真是羡慕你们啊。\n',
            '因为我是独生女。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040900V#049F所以呢，\n',
            '我一直很向往这样的家庭气氛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040901V#000F#2P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040902V#045F啊，没什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040903V#040F话就说到这里吧，\n',
            '我们也该继续赶路了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040904V沿着海岸街道一直走\n',
            '就可以到卢安了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040905V#006F#2PＯＫ。\n',
            '那我们走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    def _loc_1196(): pass

    label('loc_1196')

    Return()

# id: 0x0004 offset: 0x1197
@scena.Code('func_04_1197')
def func_04_1197():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12A5',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1207',
    )

    ChrTalk(
        0x0102,
        (
            '#0020040668V#010F往这边走是卢安市啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040669V要去孤儿院的话，\n',
            '得回到刚才的三岔路口才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1207(): pass

    label('loc_1207')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_128A',
    )

    ChrTalk(
        0x0101,
        (
            '#0010040670V#000F哎……\n',
            '这边是孤儿院吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040671V#010F不……\n',
            '这边是卢安市啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040672V我们回到刚才的三岔路口去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_128A(): pass

    label('loc_128A')

    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_12A5(): pass

    label('loc_12A5')

    Return()

# id: 0x0005 offset: 0x12A6
@scena.Code('func_05_12A6')
def func_05_12A6():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 4, 0x41C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 7, 0x427)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13AE',
    )

    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1323',
    )

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040673V#012F往这边走是玛诺利亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040674V要去孤儿院的话，\n',
            '得回到刚才的三岔路口才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1323(): pass

    label('loc_1323')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1393',
    )

    ChrTalk(
        0x0102,
        (
            '#0020040675V#012F（往这边是玛诺利亚……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020040676V（要去孤儿院的话，\n',
            '　得回到刚才的三岔路口才行。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1393(): pass

    label('loc_1393')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_13AE(): pass

    label('loc_13AE')

    Return()

# id: 0x0006 offset: 0x13AF
@scena.Code('func_06_13AF')
def func_06_13AF():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(-114260, -2000, 16980, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(261, 0)
    SetChrPos(0x0101, -113570, -2029, 17310, 270)
    SetChrPos(0x0105, -114690, -1960, 16400, 0)
    SetChrPos(0x0102, -115110, -2020, 17800, 135)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010061367V#582F不过，真想不到戴尔蒙市长\n',
            '会是一系列事件的幕后主使……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061368V#005F那些亲切的态度和表现，\n',
            '原来全都只是在做戏啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061369V#043F那个……\n',
            '有一点我不大清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061370V这次的事件，\n',
            '我们可以逮捕戴尔蒙市长吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061371V#004F……哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061372V#013F是啊……\n',
            '恐怕会很难啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061373V因为不干涉国家内政\n',
            '是游击士协会一贯以来的原则。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061374V要逮捕身为卢安地区负责人的现任市长，\n',
            '我想，恐怕会很难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061375V#580F等一下！\n',
            '这太不合理了吧！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061376V#015F的确不合理，\n',
            '但这是明文的规定啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061377V就是因为有这条规定，\n',
            '所以连埃雷波尼亚帝国\n',
            '也可以设立游击士协会的支部。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061378V#003F话、话是这么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061379V#012F总之先回协会\n',
            '和嘉恩先生商量一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061380V我想他会帮我们出个好主意的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061381V#002F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061382V#049F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061383V#006F没事的，不用担心！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061384V无论这次的犯人是怎样的人，\n',
            '我们一定会将他们绳之以法的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061385V#542F嗯……是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x003E, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x17CD
@scena.Code('func_07_17CD')
def func_07_17CD():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　玛西亚孤儿院',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x1810
@scena.Code('func_08_1810')
def func_08_1810():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　卢安市　　２３８塞尔矩\n',
            '西　玛诺利亚村　７４塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0x1878
@scena.Code('func_09_1878')
def func_09_1878():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 1, 0x4B9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1962',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_18EC',
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
    SetScenaFlags(ScenaFlag(0x0097, 1, 0x4B9))

    Jump('loc_195F')

    def _loc_18EC(): pass

    label('loc_18EC')

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

    def _loc_195F(): pass

    label('loc_195F')

    Jump('loc_1998')

    def _loc_1962(): pass

    label('loc_1962')

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
    WaitEffect(0x0F, 0x83)
    def _loc_1998(): pass

    label('loc_1998')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x000A offset: 0x19A6
@scena.Code('func_0A_19A6')
def func_0A_19A6():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0097, 2, 0x4BA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A90',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_1A1A',
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
    SetScenaFlags(ScenaFlag(0x0097, 2, 0x4BA))

    Jump('loc_1A8D')

    def _loc_1A1A(): pass

    label('loc_1A1A')

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

    def _loc_1A8D(): pass

    label('loc_1A8D')

    Jump('loc_1AC6')

    def _loc_1A90(): pass

    label('loc_1A90')

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
    WaitEffect(0x0F, 0x84)
    def _loc_1AC6(): pass

    label('loc_1AC6')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
