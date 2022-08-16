import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2305_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2305   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2305.x'
    header.mapIndex       = 1
    header.bgm            = 33
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
        ('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP'),
        ('ED6_DT29/CH12380._CH', 'ED6_DT29/CH12380P._CP'),
        ('ED6_DT09/CH10910._CH', 'ED6_DT09/CH10910P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT27/CH04520._CH', 'ED6_DT27/CH04520P._CP'),
        ('ED6_DT27/CH04525._CH', 'ED6_DT27/CH04525P._CP'),
        ('ED6_DT27/CH04526._CH', 'ED6_DT27/CH04526P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT27/CH03523._CH', 'ED6_DT27/CH03523P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
        ('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP'),
    ]

# id: 0x10001 offset: 0x16A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '幻惑之铃露茜奥拉',
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
        ScenaNpcData(
            name                = '无形迷雾',
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
            name                = '气雾兽',
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
            name                = '福音',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 458755,
            chipIndex           = 3,
            npcIndex            = 0x01E6,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1EA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_209',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x21),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_03_3E6)

    Jump('loc_241')

    def _loc_209(): pass

    label('loc_209')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_228',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x70),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_04_588)

    Jump('loc_241')

    def _loc_228(): pass

    label('loc_228')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 3, 0x1E13)),
            Expr.Return,
        ),
        'loc_241',
    )

    MapSetFlags(0x10000000)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Event(0, func_05_842)

    def _loc_241(): pass

    label('loc_241')

    Return()

# id: 0x0001 offset: 0x242
@scena.Code('func_01_242')
def func_01_242():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C0, 1, 0x1E01)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_253',
    )

    PlaySE(235, 0x01, 0x50)

    def _loc_253(): pass

    label('loc_253')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x456),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_268',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x6F),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_268(): pass

    label('loc_268')

    Return()

# id: 0x0002 offset: 0x269
@scena.Code('func_02_269')
def func_02_269():
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
        'loc_28E',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3D0')

    def _loc_28E(): pass

    label('loc_28E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2A7',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3D0')

    def _loc_2A7(): pass

    label('loc_2A7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C0',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3D0')

    def _loc_2C0(): pass

    label('loc_2C0')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2D9',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3D0')

    def _loc_2D9(): pass

    label('loc_2D9')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F2',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3D0')

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_30B',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3D0')

    def _loc_30B(): pass

    label('loc_30B')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_324',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_3D0')

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_3D0')

    def _loc_33D(): pass

    label('loc_33D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_356',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_3D0')

    def _loc_356(): pass

    label('loc_356')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36F',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_3D0')

    def _loc_36F(): pass

    label('loc_36F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_388',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_3D0')

    def _loc_388(): pass

    label('loc_388')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A1',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_3D0')

    def _loc_3A1(): pass

    label('loc_3A1')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3BA',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_3D0')

    def _loc_3BA(): pass

    label('loc_3BA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3D0',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_3D0(): pass

    label('loc_3D0')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3E5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3D0')

    def _loc_3E5(): pass

    label('loc_3E5')

    Return()

# id: 0x0003 offset: 0x3E6
@scena.Code('func_03_3E6')
def func_03_3E6():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(19060, 250, 11220, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4370, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    PlaySE(451, 0x00, 0x64)
    ChrSetPos(0x0008, -1120, 250, 10980, 180)
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 1)
    StopEffect(0x80, 0x00)
    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)
    OP_71(0x0004, 0x0004)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    Sleep(1000)

    @scena.Lambda('lambda_04A9')
    def lambda_04A9():
        CameraMove(2600, 250, 13480, 4000)

        ExitThread()

    DispatchAsync(0x000B, 0x0000, lambda_04A9)

    OP_C8(0x0200, 0x0046, 'C_PLAC20._CH', 0x01, 0x03E8)
    FadeIn(1000, 0)
    WaitForThreadExit(0x000B, 0x0000)
    Sleep(1000)

    Fade(1000)
    CameraMove(-1530, 0, 15630, 0)
    OP_67(0, 4400, -10000, 0)
    CameraSetDistance(5730, 0)
    OP_6C(332000, 0)
    OP_6E(155, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210340005V#240F#5P这里是『幻惑之铃』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210340006V『β』的设置完成了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C1705._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x588
@scena.Code('func_04_588')
def func_04_588():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(1220, 950, 14960, 0)
    OP_67(0, 8600, -10000, 0)
    CameraSetDistance(2830, 0)
    OP_6C(45000, 0)
    OP_6E(408, 0)
    ChrSetPos(0x0008, -1120, 250, 10980, 180)
    ChrSetFlags(0x0008, 0x0004)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 1)
    OP_E5(0x08, 0x00, 0x00)
    StopEffect(0x80, 0x00)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_6F(0x0000, 60)
    OP_6F(0x0001, 60)
    OP_6F(0x0002, 60)
    OP_6F(0x0003, 60)
    OP_6F(0x0004, 60)
    OP_70(0x0000, 60)
    OP_70(0x0001, 60)
    OP_70(0x0002, 60)
    OP_70(0x0003, 60)
    OP_E8(0xD0, 0x07, 0x00, 0x00)
    LoadEffect(0x01, 'map\\\\mp061_00.eff')
    PlayEffect(0x01, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    FadeIn(1000, 0)
    OP_0D()
    Sleep(1000)

    OP_B0(0x0000, 0x50)
    OP_B0(0x0001, 0x50)
    OP_B0(0x0002, 0x50)
    OP_B0(0x0003, 0x50)
    OP_B0(0x0004, 0x50)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)
    OP_73(0x0001)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)
    OP_73(0x0002)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0)
    OP_73(0x0003)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0)
    OP_73(0x0004)
    PlaySE(153, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_79(0x00, 0x0001)
    OP_79(0x01, 0x0001)
    OP_79(0x02, 0x0001)
    OP_79(0x03, 0x0001)
    OP_79(0x04, 0x0001)
    OP_7B()
    Fade(1000)
    OP_11(0xA0, 0xB4, 0xFF, 98000, 233000, 0)
    CameraMove(-32090, 30000, -26260, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(300, 0)
    OP_0D()
    LoadEffect(0x00, 'map\\mp049_03.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, -32090, 30000, -26260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(312, 0x00, 0x64)
    Sleep(3000)

    MapSetFlags(0x02000000)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_E8(0xE8, 0x03, 0x00, 0x00)
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/C1705._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0x842
@scena.Code('func_05_842')
def func_05_842():
    Call(0, 0x0006)
    Call(0, 0x0007)

    Return()

# id: 0x0006 offset: 0x84B
@scena.Code('func_06_84B')
def func_06_84B():
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
        'loc_862',
    )

    Call(0, 0x0008)
    Call(0, 0x0009)

    def _loc_862(): pass

    label('loc_862')

    CameraMove(6870, 6810, 600, 0)
    OP_67(0, 4710, -10000, 0)
    CameraSetDistance(2480, 0)
    OP_6C(56000, 0)
    OP_6E(386, 0)
    ChrSetPos(0x0008, 900, 950, 12280, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, 740, -1750, -7480, 0)
    ChrSetPos(0x0102, -650, -1750, -7480, 0)
    ChrSetPos(0x0103, 820, -1750, -7480, 0)
    ChrSetPos(0x00F9, -750, -1750, -7480, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0103, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x00F9, 0x0080)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0000, 8)
    OP_70(0x0001, 8)
    OP_70(0x0002, 8)
    OP_70(0x0003, 8)
    OP_70(0x0004, 8)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_71(0x0005, 0x0004)

    @scena.Lambda('lambda_09A7')
    def lambda_09A7():
        CameraMove(430, 0, -2500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_09A7)

    @scena.Lambda('lambda_09BF')
    def lambda_09BF():
        OP_67(0, 8960, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09BF)

    @scena.Lambda('lambda_09D7')
    def lambda_09D7():
        CameraSetDistance(2300, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_09D7)

    @scena.Lambda('lambda_09E7')
    def lambda_09E7():
        OP_6C(45000, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_09E7)

    @scena.Lambda('lambda_09F7')
    def lambda_09F7():
        OP_6E(307, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_09F7)

    FadeIn(1000, 0)
    Sleep(4000)

    ChrClearFlags(0x0101, 0x0080)

    @scena.Lambda('lambda_0A1A')
    def lambda_0A1A():
        ChrWalkTo(0x00FE, 900, 0, -2040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0A1A)

    Sleep(100)

    ChrClearFlags(0x0102, 0x0080)

    @scena.Lambda('lambda_0A3F')
    def lambda_0A3F():
        ChrWalkTo(0x00FE, -450, 0, -2009, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A3F)

    Sleep(600)

    ChrClearFlags(0x0103, 0x0080)

    @scena.Lambda('lambda_0A64')
    def lambda_0A64():
        ChrWalkTo(0x00FE, 850, 0, -3520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0A64)

    Sleep(100)

    ChrClearFlags(0x00F9, 0x0080)

    @scena.Lambda('lambda_0A89')
    def lambda_0A89():
        ChrWalkTo(0x00FE, -500, 0, -3590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0A89)

    WaitForThreadExit(0x00F9, 0x0001)

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0210341314V呵呵……\n',
            '好像稍微有些迟到了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B5A',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B98')

    def _loc_B5A(): pass

    label('loc_B5A')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B81',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B98')

    def _loc_B81(): pass

    label('loc_B81')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B98(): pass

    label('loc_B98')

    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030341315V#022F姐姐……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(200)

    PlayBGM(111)
    Sleep(500)

    @scena.Lambda('lambda_0BD0')
    def lambda_0BD0():
        CameraMove(1160, 950, 13010, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BD0)

    @scena.Lambda('lambda_0BE8')
    def lambda_0BE8():
        OP_67(0, 5350, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0BE8)

    @scena.Lambda('lambda_0C00')
    def lambda_0C00():
        OP_6E(337, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0C00)

    WaitForThreadExit(0x0101, 0x0003)
    ChrSetPos(0x0103, 740, -1750, -7480, 0)
    ChrSetPos(0x0102, -650, -1750, -7480, 0)
    ChrSetPos(0x0101, 820, -1750, -7480, 0)
    ChrSetPos(0x00F9, -750, -1750, -7480, 0)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 7)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x0103, 11)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_C8E'),
        (0x00000004, 'loc_C9B'),
        (0x00000006, 'loc_CA8'),
        (0x00000007, 'loc_CB5'),
        (0x00000008, 'loc_CC2'),
        (-1, 'loc_CCF'),
    )

    def _loc_C8E(): pass

    label('loc_C8E')

    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 14)

    Jump('loc_CCF')

    def _loc_C9B(): pass

    label('loc_C9B')

    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0105, 16)

    Jump('loc_CCF')

    def _loc_CA8(): pass

    label('loc_CA8')

    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 18)

    Jump('loc_CCF')

    def _loc_CB5(): pass

    label('loc_CB5')

    ChrSetSubChip(0x0108, 0)
    ChrSetChipByIndex(0x0108, 20)

    Jump('loc_CCF')

    def _loc_CC2(): pass

    label('loc_CC2')

    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x0109, 22)

    Jump('loc_CCF')

    def _loc_CCF(): pass

    label('loc_CCF')

    @scena.Lambda('lambda_0CD5')
    def lambda_0CD5():
        ChrWalkTo(0x00FE, -80, 0, 4000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_0CD5)

    Sleep(300)

    @scena.Lambda('lambda_0CF5')
    def lambda_0CF5():
        ChrWalkTo(0x00FE, 1010, 0, 3340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0CF5)

    Sleep(100)

    @scena.Lambda('lambda_0D15')
    def lambda_0D15():
        ChrWalkTo(0x00FE, -1400, 0, 2790, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0D15)

    Sleep(200)

    @scena.Lambda('lambda_0D35')
    def lambda_0D35():
        ChrWalkTo(0x00FE, -360, 0, 2190, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0D35)

    Fade(500)
    CameraMove(1610, 500, 9000, 0)
    OP_67(0, 2630, -10000, 0)
    CameraSetDistance(2380, 0)
    OP_6C(29000, 0)
    OP_6E(452, 0)
    OP_0D()
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210341316V#240F欢迎，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341317V还有约修亚……\n',
            '好久不见，真令人高兴啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341318V#1042F#6P露茜奥拉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341319V为什么你会\n',
            '协助教授？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020341320V我还以为你和教授的关系\n',
            '没那么好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341321V#244F因为这里是我\n',
            '巡回修业时曾经造访过的留恋之地……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341322V#241F所以忍不住来了兴致，\n',
            '也就是这样的吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341323V#1005F#4P既、既然是留恋之地，\n',
            '为什么还要帮教授做这种事！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010341324V也不顾忌一下雪拉姐的心情……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341325V#522F#6P艾丝蒂尔……算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341326V#022F光是动嘴，\n',
            '姐姐是不会回答你任何问题的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341327V除非我证明给她看\n',
            '我的实力值得她回答。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341328V#241F哎呀……呵呵呵。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341329V不愧是雪拉，\n',
            '果然很了解我嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341330V#524F#6P以前姐姐教我技艺的时候\n',
            '也总是这个样子的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341331V#026F所以姐姐……答应我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341332V#024F如果我能够证明自己实力的话，\n',
            '那你就告诉我\n',
            '为什么要帮助『结社』……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341333V#244F呵呵……好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    CameraMove(1000, 750, 11580, 0)
    OP_67(0, 2320, -10000, 0)
    CameraSetDistance(3240, 0)
    OP_6C(8000, 0)
    OP_6E(333, 0)
    CameraMove(1000, 750, 11580, 0)
    OP_67(0, 2280, -10000, 0)
    CameraSetDistance(3380, 0)
    OP_6C(8000, 0)
    OP_6E(333, 0)
    ChrSetPos(0x0103, 100, 0, 3510, 0)
    ChrSetPos(0x0102, -1200, 0, 2900, 0)
    ChrSetPos(0x0101, 1000, 0, 2800, 0)
    ChrSetPos(0x00F9, -500, 0, 1500, 0)
    OP_0D()
    Sleep(200)

    Fade(250)
    ChrSetSubChip(0x0008, 3)
    ChrSetChipByIndex(0x0008, 5)
    OP_0D()
    LoadEffect(0x01, 'scraft\\sc040_08.eff')
    PlayEffect(0x01, 0x00, 0x00FF, -46660, 1000, 19260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(613, 0x00, 0x64)
    Sleep(2000)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 6)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(240)

    Fade(500)
    StopEffect(0x00, 0x02)
    CreateThread(0x0009, 0x03, 0x00, func_02_269)
    ChrSetPos(0x0009, 2800, 2500, 9650, 180)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetFlags(0x0009, 0x0004)
    ChrClearFlags(0x0009, 0x0080)
    CreateThread(0x000A, 0x03, 0x00, func_02_269)
    ChrSetPos(0x000A, -1200, 2500, 10500, 180)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)
    ChrSetFlags(0x000A, 0x0004)
    ChrClearFlags(0x000A, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_1308')
    def lambda_1308():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1308)

    @scena.Lambda('lambda_131A')
    def lambda_131A():
        ChrMoveTo(0x00FE, 2800, 1500, 9650, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_131A)

    Sleep(800)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_1344')
    def lambda_1344():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1344)

    @scena.Lambda('lambda_1356')
    def lambda_1356():
        ChrMoveTo(0x00FE, -1200, 1500, 10500, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1356)

    Sleep(800)

    PlaySE(538, 0x00, 0x64)
    Sleep(800)

    PlaySE(538, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_13F0',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_142E')

    def _loc_13F0(): pass

    label('loc_13F0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1417',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_142E')

    def _loc_1417(): pass

    label('loc_1417')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_142E(): pass

    label('loc_142E')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010341334V#1020F#6P出，出现了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341335V#1042F#6P善鬼与护鬼──\n',
            '掌管阴阳的式神们！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341336V#244F这是将东方的符术\n',
            '整理以后自成一派的东西哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341337V#240F雪拉扎德。\n',
            '请让我看看。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341338V你离开我身边之后，\n',
            '在这里到底获得了多少的能力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341339V#026F#6P……明白。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341340V#024F那我就献丑了，\n',
            '看看我这『银闪』的实力吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_15A9')
    def lambda_15A9():
        CameraMove(950, 250, 11010, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_15A9)

    @scena.Lambda('lambda_15C1')
    def lambda_15C1():
        OP_67(0, 3510, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_15C1)

    @scena.Lambda('lambda_15D9')
    def lambda_15D9():
        CameraSetDistance(2780, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_15D9)

    @scena.Lambda('lambda_15E9')
    def lambda_15E9():
        ChrMoveTo(0x00FE, 710, 0, 6840, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_15E9)

    Sleep(50)

    @scena.Lambda('lambda_1609')
    def lambda_1609():
        ChrMoveTo(0x00FE, 1640, 0, 5810, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1609)

    @scena.Lambda('lambda_1624')
    def lambda_1624():
        ChrMoveTo(0x00FE, -440, 0, 5980, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1624)

    @scena.Lambda('lambda_163F')
    def lambda_163F():
        ChrMoveTo(0x00FE, -250, 100, 8000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_163F)

    Sleep(50)

    @scena.Lambda('lambda_165F')
    def lambda_165F():
        ChrMoveTo(0x00FE, 1950, 100, 8320, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_165F)

    @scena.Lambda('lambda_167A')
    def lambda_167A():
        ChrMoveTo(0x00FE, 370, 0, 4310, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_167A)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000456, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_16C5'),
        (-1, 'loc_16CA'),
    )

    def _loc_16C5(): pass

    label('loc_16C5')

    OP_B4(0x00)

    Jump('loc_16CA')

    def _loc_16CA(): pass

    label('loc_16CA')

    Return()

# id: 0x0007 offset: 0x16CB
@scena.Code('func_07_16CB')
def func_07_16CB():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0x01)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    TerminateThread(0x0103, 0x01)
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x00F9, 0x01)
    Sleep(500)

    Sleep(500)

    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 7)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x0103, 11)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_173E'),
        (0x00000004, 'loc_174B'),
        (0x00000006, 'loc_1758'),
        (0x00000007, 'loc_1765'),
        (0x00000008, 'loc_1772'),
        (-1, 'loc_177F'),
    )

    def _loc_173E(): pass

    label('loc_173E')

    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 14)

    Jump('loc_177F')

    def _loc_174B(): pass

    label('loc_174B')

    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0105, 16)

    Jump('loc_177F')

    def _loc_1758(): pass

    label('loc_1758')

    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 18)

    Jump('loc_177F')

    def _loc_1765(): pass

    label('loc_1765')

    ChrSetSubChip(0x0108, 0)
    ChrSetChipByIndex(0x0108, 20)

    Jump('loc_177F')

    def _loc_1772(): pass

    label('loc_1772')

    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x0109, 22)

    Jump('loc_177F')

    def _loc_177F(): pass

    label('loc_177F')

    ChrSetPos(0x0103, -100, 0, 5100, 0)
    ChrSetPos(0x0101, 1200, 0, 4000, 0)
    ChrSetPos(0x0102, -1020, 0, 3400, 0)
    ChrSetPos(0x00F9, 200, 0, 2300, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 900, 950, 12280, 180)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 4)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_70(0x0000, 8)
    OP_70(0x0001, 8)
    OP_70(0x0002, 8)
    OP_70(0x0003, 8)
    OP_70(0x0004, 8)
    LoadEffect(0x00, 'map\\\\mp061_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, 0, 1300, 13650, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(500)

    CameraMove(1280, 950, 9610, 0)
    OP_67(0, 4910, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(344, 0)
    OP_71(0x0005, 0x0004)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210341341V#243F哎呀……\n',
            '我的式神竟然被打倒了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341342V#240F是拜『剑圣』的指导所赐吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010341343V#1022F#4P呼呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341344V#024F#6P姐姐……如何！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341345V#240F呵呵……\n',
            '作为你努力的褒奖，我就告诉你吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341346V#244F我加入『结社』……\n',
            '是想看清自己的黑暗面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341347V#023F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(500)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0101, 7)
    ChrSetSubChip(0x0102, 0)
    ChrSetChipByIndex(0x0102, 9)
    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x0103, 11)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_1A59'),
        (0x00000004, 'loc_1A66'),
        (0x00000006, 'loc_1A73'),
        (0x00000007, 'loc_1A80'),
        (0x00000008, 'loc_1A8D'),
        (-1, 'loc_1A9A'),
    )

    def _loc_1A59(): pass

    label('loc_1A59')

    ChrSetSubChip(0x0106, 0)
    ChrSetChipByIndex(0x0106, 14)

    Jump('loc_1A9A')

    def _loc_1A66(): pass

    label('loc_1A66')

    ChrSetSubChip(0x0105, 0)
    ChrSetChipByIndex(0x0105, 16)

    Jump('loc_1A9A')

    def _loc_1A73(): pass

    label('loc_1A73')

    ChrSetSubChip(0x0107, 0)
    ChrSetChipByIndex(0x0107, 18)

    Jump('loc_1A9A')

    def _loc_1A80(): pass

    label('loc_1A80')

    ChrSetSubChip(0x0108, 0)
    ChrSetChipByIndex(0x0108, 20)

    Jump('loc_1A9A')

    def _loc_1A8D(): pass

    label('loc_1A8D')

    ChrSetSubChip(0x0109, 0)
    ChrSetChipByIndex(0x0109, 22)

    Jump('loc_1A9A')

    def _loc_1A9A(): pass

    label('loc_1A9A')

    CameraMove(110, 250, 12650, 0)
    OP_67(0, 3200, -10000, 0)
    CameraSetDistance(3420, 0)
    OP_6C(0, 0)
    OP_6E(344, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210341348V#242F#5P８年前……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341349V团长从悬崖摔落\n',
            '而亡的事你还记得吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341350V#024F当、当然记得。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341351V由于那个事故，\n',
            '我们哈维剧团的全体团员都……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341352V#244F#5P对……剧团解散，\n',
            '大家都各奔东西了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341353V但是，为何团长会独自一人\n',
            '去那种渺无人烟的地方，\n',
            '到最后谁也不明白……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341354V#240F你觉得这到底是怎么回事？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341355V#023F怎、怎么回事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_21()

    ChrTalk(
        0x0008,
        (
            '#0210341356V#244F#5P答案很简单……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341357V#241F那时，团长并不是\n',
            '独自一人呆在悬崖附近。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341358V我就在他旁边……\n',
            '并且把他推了下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D10')
    def lambda_1D10():
        CameraSetDistance(3200, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D10)

    Sleep(200)

    PlayBGM(83)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030341359V#023F#6P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341360V……什么……\n',
            '你在说什么呢，姐姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341361V#241F#5P呵呵，我不是说了吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341362V哈维团长\n',
            '是我亲手杀死的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341363V#524F#6P啊哈哈……玩笑开过火了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341364V因为那个时候，姐姐你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341365V#244F#5P亲手杀害团长后\n',
            '我一脸平静地回到大家身边。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341366V然后就鸣响了铃铛，\n',
            '让大家听到团长在喊叫的幻音。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341367V#241F──利用我的幻术，\n',
            '要制造这点小把戏简直是轻而易举的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341368V#527F#6P住口……别再说了啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341369V姐姐竟然杀了团长……\n',
            '怎么可能有这种事！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030341370V#024F你们就像真正的父女一样……\n',
            '甚至比真正的父女还要亲密！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210341371V#242F#5P正因为如此，我才不能饶恕他。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210341372V他竟然打算\n',
            '离开我们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341373V#023F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x02)
    Sleep(500)

    PlaySE(153, 0x00, 0x64)
    OP_23(0x00EB)
    OP_1F(0x5A, 0x000007D0)
    Fade(500)
    CameraSetDistance(3000, 0)
    StopEffect(0x00, 0x02)
    StopEffect(0x81, 0x02)
    PlayEffect(0x82, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    StopEffect(0x83, 0x02)
    PlayEffect(0x84, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_79(0x00, 0x0002)
    OP_79(0x01, 0x0002)
    OP_79(0x02, 0x0002)
    OP_79(0x03, 0x0002)
    OP_79(0x04, 0x0002)
    OP_7B()
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_216F',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_21AD')

    def _loc_216F(): pass

    label('loc_216F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2196',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_21AD')

    def _loc_2196(): pass

    label('loc_2196')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_21AD(): pass

    label('loc_21AD')

    Sleep(1000)

    @scena.Lambda('lambda_21B8')
    def lambda_21B8():
        CameraMove(-250, 200, 17430, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_21B8)

    @scena.Lambda('lambda_21D0')
    def lambda_21D0():
        OP_67(0, 3660, -10000, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21D0)

    @scena.Lambda('lambda_21E8')
    def lambda_21E8():
        CameraSetDistance(3460, 2500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21E8)

    ChrSetDirection(0x0008, 270, 400)
    ChrSetDirection(0x0008, 0, 400)
    WaitForThreadExit(0x0101, 0x0000)
    OP_72(0x0000, 0x0020)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 60)
    Sleep(500)

    OP_72(0x0001, 0x0020)
    OP_6F(0x0001, 0)
    OP_70(0x0001, 60)
    Sleep(100)

    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 0)
    OP_70(0x0002, 60)
    Sleep(100)

    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 0)
    OP_70(0x0003, 60)
    Sleep(100)

    OP_72(0x0004, 0x0020)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 60)

    ChrTalk(
        0x0101,
        (
            '#0010341374V#1020F#5P又……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22D4',
    )

    ChrTalk(
        0x0106,
        (
            '#0050341375V#054F#5P恢复了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B8')

    def _loc_22D4(): pass

    label('loc_22D4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_230D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070341376V#065F#5P恢复了……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B8')

    def _loc_230D(): pass

    label('loc_230D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2348',
    )

    ChrTalk(
        0x0105,
        (
            '#0060341377V#043F#5P恢复了吗……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B8')

    def _loc_2348(): pass

    label('loc_2348')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2381',
    )

    ChrTalk(
        0x0108,
        (
            '#0080341378V#072F#5P恢复了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23B8')

    def _loc_2381(): pass

    label('loc_2381')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23B8',
    )

    ChrTalk(
        0x0109,
        (
            '#0180341379V#1069F#5P恢复了吗……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_23B8(): pass

    label('loc_23B8')

    Sleep(300)

    OP_1F(0x64, 0x000007D0)
    Fade(1000)
    CameraMove(5030, 3860, 11650, 0)
    OP_67(0, 1590, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(45000, 0)
    OP_6E(363, 0)
    OP_0D()

    @scena.Lambda('lambda_240C')
    def lambda_240C():
        CameraSetDistance(5500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_240C)

    Sleep(500)

    PlaySE(313, 0x00, 0x64)
    LoadEffect(0x02, 'map\\mp049_02.eff')
    PlayEffect(0x02, 0x02, 0x00FF, 0, 0, 6720, 0, 0, 0, 550, 550, 550, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    StopEffect(0x80, 0x00)
    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C2307._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2492
@scena.Code('func_08_2492')
def func_08_2492():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        (0x00000000, 'loc_250C'),
        (0x00000001, 'loc_2512'),
        (-1, 'loc_2518'),
    )

    def _loc_250C(): pass

    label('loc_250C')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_2518')

    def _loc_2512(): pass

    label('loc_2512')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_2518')

    def _loc_2518(): pass

    label('loc_2518')

    Return()

# id: 0x0009 offset: 0x2519
@scena.Code('func_09_2519')
def func_09_2519():
    FadeOut(0, 0, -1)
    CameraMove(-66940, 250, 36210, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(3700, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            ChrTable['雪拉扎德'],
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['提妲'],
            ChrTable['科洛丝'],
            ChrTable['凯文神父'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
