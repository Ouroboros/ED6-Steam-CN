import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4202_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4202   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4202.x'
    header.mapIndex       = 1
    header.bgm            = 31
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
        ('ED6_DT09/CH10490._CH', 'ED6_DT09/CH10490P._CP'),
        ('ED6_DT09/CH10491._CH', 'ED6_DT09/CH10491P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
        ('ED6_DT09/CH10510._CH', 'ED6_DT09/CH10510P._CP'),
        ('ED6_DT09/CH10511._CH', 'ED6_DT09/CH10511P._CP'),
        ('ED6_DT09/CH11110._CH', 'ED6_DT09/CH11110P._CP'),
        ('ED6_DT09/CH11111._CH', 'ED6_DT09/CH11111P._CP'),
        ('ED6_DT09/CH11120._CH', 'ED6_DT09/CH11120P._CP'),
        ('ED6_DT09/CH11121._CH', 'ED6_DT09/CH11121P._CP'),
        ('ED6_DT09/CH11130._CH', 'ED6_DT09/CH11130P._CP'),
        ('ED6_DT09/CH11131._CH', 'ED6_DT09/CH11131P._CP'),
        ('ED6_DT09/CH11140._CH', 'ED6_DT09/CH11140P._CP'),
        ('ED6_DT09/CH11141._CH', 'ED6_DT09/CH11141P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
    ]

# id: 0x10001 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 12,
            chipIndex           = 12,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x16A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 13590,
            z           = 0,
            y           = 67390,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 13650,
            z           = 0,
            y           = 73480,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 13600,
            z           = 0,
            y           = 79600,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 13660,
            z           = 0,
            y           = 83670,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 13620,
            z           = 0,
            y           = 90730,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 60960,
            z           = 0,
            y           = 94820,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 100830,
            z           = 0,
            y           = 20580,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0272,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 38210,
            z           = 0,
            y           = -520,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 15760,
            z           = 0,
            y           = -10320,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 34200,
            z           = 0,
            y           = 7700,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 30560,
            z           = 0,
            y           = -65610,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x29E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x29E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 43930,
            triggerZ            = 0,
            triggerY            = -6210,
            triggerRange        = 1000,
            actorX              = 43860,
            actorZ              = 1500,
            actorY              = -5600,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 41920,
            triggerZ            = 450,
            triggerY            = 124030,
            triggerRange        = 1000,
            actorX              = 41950,
            actorZ              = 1950,
            actorY              = 123110,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 29340,
            triggerZ            = 0,
            triggerY            = 130710,
            triggerRange        = 1000,
            actorX              = 28570,
            actorZ              = 1500,
            actorY              = 130759,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x30A
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_316'),
        (-1, 'loc_32C'),
    )

    def _loc_316(): pass

    label('loc_316')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 4, 0x65C)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_329',
    )

    SetScenaFlags(ScenaFlag(0x00CB, 4, 0x65C))
    Event(0, func_03_44C)

    def _loc_329(): pass

    label('loc_329')

    Jump('loc_32C')

    def _loc_32C(): pass

    label('loc_32C')

    Return()

# id: 0x0001 offset: 0x32D
@scena.Code('func_01_32D')
def func_01_32D():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 0, 0x6D8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_33F',
    )

    OP_6F(0x0000, 0)

    Jump('loc_346')

    def _loc_33F(): pass

    label('loc_33F')

    OP_6F(0x0000, 60)

    def _loc_346(): pass

    label('loc_346')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 2, 0x6DA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_358',
    )

    OP_6F(0x0001, 0)

    Jump('loc_35F')

    def _loc_358(): pass

    label('loc_358')

    OP_6F(0x0001, 60)

    def _loc_35F(): pass

    label('loc_35F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 4, 0x6DC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_371',
    )

    OP_6F(0x0002, 0)

    Jump('loc_378')

    def _loc_371(): pass

    label('loc_371')

    OP_6F(0x0002, 60)

    def _loc_378(): pass

    label('loc_378')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x37E
@scena.Code('func_02_37E')
def func_02_37E():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
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
        'loc_3A3',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_436')

    def _loc_3A3(): pass

    label('loc_3A3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BC',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_436')

    def _loc_3BC(): pass

    label('loc_3BC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D5',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_436')

    def _loc_3D5(): pass

    label('loc_3D5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3EE',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_436')

    def _loc_3EE(): pass

    label('loc_3EE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_407',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_436')

    def _loc_407(): pass

    label('loc_407')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_420',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_436')

    def _loc_420(): pass

    label('loc_420')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_436',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_436(): pass

    label('loc_436')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_44B',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_436')

    def _loc_44B(): pass

    label('loc_44B')

    Return()

# id: 0x0003 offset: 0x44C
@scena.Code('func_03_44C')
def func_03_44C():
    EventBegin(0x00)
    CameraMove(100690, 250, 128360, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0104, 100890, 2000, 130110, 180)
    ChrSetPos(0x0108, 101450, 2000, 131240, 180)
    ChrSetPos(0x0102, 100530, 2000, 131390, 180)

    @scena.Lambda('lambda_04C4')
    def lambda_04C4():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_04C4')

    DispatchAsync2(0x0108, 0x0001, lambda_04C4)

    @scena.Lambda('lambda_04D5')
    def lambda_04D5():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_04D5')

    DispatchAsync2(0x0102, 0x0001, lambda_04D5)

    @scena.Lambda('lambda_04E6')
    def lambda_04E6():
        ChrWalkTo(0x00FE, 100860, 0, 127680, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_04E6)

    @scena.Lambda('lambda_0501')
    def lambda_0501():
        ChrWalkTo(0x00FE, 100600, 0, 127720, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0501)

    @scena.Lambda('lambda_051C')
    def lambda_051C():
        ChrWalkTo(0x00FE, 101290, 0, 126520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_051C)

    WaitForThreadExit(0x0104, 0x0001)

    @scena.Lambda('lambda_053C')
    def lambda_053C():
        ChrWalkTo(0x00FE, 98840, 0, 127070, 2500, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_053C)

    WaitForThreadExit(0x0104, 0x0001)
    ChrSetDirection(0x0104, 90, 400)
    WaitForThreadExit(0x0108, 0x0002)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0104,
        (
            '#0040131015V#030F那么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131016V呵呵，我们这就确认一下\n',
            '之前提到的隐藏水路的路线图吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020131017V#012F#5P没错……\n',
            '不过先等一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT04/C_VIS019._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1500)

    SetMessageWindowPos(50, 0, -1, -1)
    TalkSetChrName('金')

    Talk(
        (
            '#0080131025V',
            (TxtCtl.SetColor, 0x0),
            '#070F现在我们所处的位置\n',
            '在右下角楼梯标志的地方……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131019V图中央标有『＝』的地方\n',
            '就是隐藏水路的入口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(400, 0, -1, -1)
    TalkSetChrName('约修亚')

    Talk(
        (
            '#0020131020V#012F对……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131021V首先就到那里去，\n',
            '然后调查一下附近的墙壁吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_AE(0x000001F4)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_28(0x004D, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x715
@scena.Code('func_04_715')
def func_04_715():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 0, 0x6D8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8B9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 1, 0x6D9)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7F1',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 43860, 3000, -5600, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_0764')
    def lambda_0764():
        ChrMoveTo(0x00FE, 43860, 1500, -5600, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0764)

    @scena.Lambda('lambda_077F')
    def lambda_077F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_077F)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000279, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_7CC'),
        (0x00000002, 'loc_7DE'),
        (0x00000001, 'loc_7EE'),
        (-1, 'loc_7F1'),
    )

    def _loc_7CC(): pass

    label('loc_7CC')

    SetScenaFlags(ScenaFlag(0x00DB, 1, 0x6D9))
    OP_6F(0x0000, 60)
    Sleep(500)

    Jump('loc_7F1')

    def _loc_7DE(): pass

    label('loc_7DE')

    OP_6F(0x0000, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_7EE(): pass

    label('loc_7EE')

    OP_B4(0x00)

    Return()

    def _loc_7F1(): pass

    label('loc_7F1')

    If(
        (
            (Expr.Eval, "AddItem(0x005D, 1)"),
            Expr.Return,
        ),
        'loc_845',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '鹰眼枪',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DB, 0, 0x6D8))

    Jump('loc_8B6')

    def _loc_845(): pass

    label('loc_845')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '鹰眼枪',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '鹰眼枪',
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

    def _loc_8B6(): pass

    label('loc_8B6')

    Jump('loc_8EF')

    def _loc_8B9(): pass

    label('loc_8B9')

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
    WaitEffect(0x0F, 0x47)
    def _loc_8EF(): pass

    label('loc_8EF')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x8FD
@scena.Code('func_05_8FD')
def func_05_8FD():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 2, 0x6DA)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AAD',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 3, 0x6DB)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9D9',
    )

    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetPos(0x0008, 41950, 3450, 123110, 320)
    ChrTurnDirection(0x0008, 0x0000, 0)

    @scena.Lambda('lambda_094C')
    def lambda_094C():
        ChrMoveTo(0x00FE, 41950, 1950, 123110, 1200, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_094C)

    @scena.Lambda('lambda_0967')
    def lambda_0967():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1200)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0967)

    ChrClearFlags(0x0008, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '魔兽出现了！',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    Battle(0x00000279, 0x00000000, 0x00, 0x0000, 0xFF)
    ChrSetFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_9B4'),
        (0x00000002, 'loc_9C6'),
        (0x00000001, 'loc_9D6'),
        (-1, 'loc_9D9'),
    )

    def _loc_9B4(): pass

    label('loc_9B4')

    SetScenaFlags(ScenaFlag(0x00DB, 3, 0x6DB))
    OP_6F(0x0001, 60)
    Sleep(500)

    Jump('loc_9D9')

    def _loc_9C6(): pass

    label('loc_9C6')

    OP_6F(0x0001, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

    def _loc_9D6(): pass

    label('loc_9D6')

    OP_B4(0x00)

    Return()

    def _loc_9D9(): pass

    label('loc_9D9')

    If(
        (
            (Expr.Eval, "AddItem(0x0146, 1)"),
            Expr.Return,
        ),
        'loc_A31',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '斗魂扎头巾',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DB, 2, 0x6DA))

    Jump('loc_AAA')

    def _loc_A31(): pass

    label('loc_A31')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '斗魂扎头巾',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '斗魂扎头巾',
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

    def _loc_AAA(): pass

    label('loc_AAA')

    Jump('loc_AE3')

    def _loc_AAD(): pass

    label('loc_AAD')

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
    WaitEffect(0x0F, 0x48)
    def _loc_AE3(): pass

    label('loc_AE3')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0xAF1
@scena.Code('func_06_AF1')
def func_06_AF1():
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 4, 0x6DC)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_BE1',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_B67',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DB, 4, 0x6DC))

    Jump('loc_BDE')

    def _loc_B67(): pass

    label('loc_B67')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
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

    def _loc_BDE(): pass

    label('loc_BDE')

    Jump('loc_C17')

    def _loc_BE1(): pass

    label('loc_BE1')

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
    WaitEffect(0x0F, 0x49)
    def _loc_C17(): pass

    label('loc_C17')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
