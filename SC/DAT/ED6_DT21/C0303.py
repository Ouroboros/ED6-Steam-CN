import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0303_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0303   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0303.x'
    header.mapIndex       = 19
    header.bgm            = 21
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
        ('ED6_DT29/CH12380._CH', 'ED6_DT29/CH12380P._CP'),
        ('ED6_DT09/CH10910._CH', 'ED6_DT09/CH10910P._CP'),
        ('ED6_DT06/CH20021._CH', 'ED6_DT06/CH20021P._CP'),
        ('ED6_DT27/CH03004._CH', 'ED6_DT27/CH03004P._CP'),
        ('ED6_DT07/CH00054._CH', 'ED6_DT07/CH00054P._CP'),
        ('ED6_DT07/CH00064._CH', 'ED6_DT07/CH00064P._CP'),
        ('ED6_DT07/CH00034._CH', 'ED6_DT07/CH00034P._CP'),
        ('ED6_DT07/CH00044._CH', 'ED6_DT07/CH00044P._CP'),
        ('ED6_DT07/CH00074._CH', 'ED6_DT07/CH00074P._CP'),
        ('ED6_DT26/CH20235._CH', 'ED6_DT26/CH20235P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT29/CH12381._CH', 'ED6_DT29/CH12381P._CP'),
        ('ED6_DT09/CH10911._CH', 'ED6_DT09/CH10911P._CP'),
    ]

# id: 0x10001 offset: 0x18A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '气雾兽',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '无形迷雾',
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
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x01E5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '残像',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x01E5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '幻惑之铃露茜奥拉',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x22A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x22A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -50270,
            y           = -1000,
            z           = 12650,
            range       = -44030,
            dword_10    = 0x000007D0,
            dword_14    = 0x00002652,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x24A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 53690,
            triggerZ            = 360,
            triggerY            = 7930,
            triggerRange        = 1000,
            actorX              = 57030,
            actorZ              = -1000,
            actorY              = 7730,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x26E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27D',
    )

    Event(0, func_03_685)

    Jump('loc_2B8')

    def _loc_27D(): pass

    label('loc_27D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_28E',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_05_D43)

    Jump('loc_2B8')

    def _loc_28E(): pass

    label('loc_28E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_2A8',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_08_2279)

    Jump('loc_2B8')

    def _loc_2A8(): pass

    label('loc_2A8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 4, 0x1824)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 5, 0x1825)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B8',
    )

    Event(0, func_04_A3C)

    def _loc_2B8(): pass

    label('loc_2B8')

    Return()

# id: 0x0001 offset: 0x2B9
@scena.Code('func_01_2B9')
def func_01_2B9():
    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x45F),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CE',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_2CE(): pass

    label('loc_2CE')

    StopEffect(0x86, 0x00)
    StopEffect(0x87, 0x00)
    StopEffect(0x88, 0x00)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4FB',
    )

    OP_C4(0x00, 0x00000004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_4FB',
    )

    MapSetFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0, 60000, 0)
    LoadEffect(0x00, 'map\\\\mp073_00.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -54310, -110, 10630, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x01, 0x00FF, -51620, -110, 7230, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x02, 0x00FF, -49800, -110, 8380, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x03, 0x00FF, -44290, -110, 8029, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x04, 0x00FF, -40610, -110, 10800, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0x05, 0x00FF, -40940, 270, 7260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x87, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x88, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)

    def _loc_4FB(): pass

    label('loc_4FB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_507',
    )

    OP_64(0x00, 0x0001)

    def _loc_507(): pass

    label('loc_507')

    Return()

# id: 0x0002 offset: 0x508
@scena.Code('func_02_508')
def func_02_508():
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
        'loc_52D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_66F')

    def _loc_52D(): pass

    label('loc_52D')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_546',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_66F')

    def _loc_546(): pass

    label('loc_546')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_55F',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_66F')

    def _loc_55F(): pass

    label('loc_55F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_578',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_66F')

    def _loc_578(): pass

    label('loc_578')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_591',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_66F')

    def _loc_591(): pass

    label('loc_591')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5AA',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_66F')

    def _loc_5AA(): pass

    label('loc_5AA')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5C3',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_66F')

    def _loc_5C3(): pass

    label('loc_5C3')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5DC',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_66F')

    def _loc_5DC(): pass

    label('loc_5DC')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_5F5',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_66F')

    def _loc_5F5(): pass

    label('loc_5F5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_60E',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_66F')

    def _loc_60E(): pass

    label('loc_60E')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_627',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_66F')

    def _loc_627(): pass

    label('loc_627')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_640',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_66F')

    def _loc_640(): pass

    label('loc_640')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_659',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_66F')

    def _loc_659(): pass

    label('loc_659')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_66F',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_66F(): pass

    label('loc_66F')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_684',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_66F')

    def _loc_684(): pass

    label('loc_684')

    Return()

# id: 0x0003 offset: 0x685
@scena.Code('func_03_685')
def func_03_685():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0308, 1, 0x1841)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F3',
    )

    ChrSetPos(0x0101, 49450, -350, -30730, 0)
    ChrSetPos(0x0103, 50560, -230, -31130, 0)
    ChrSetPos(0x00F8, 48880, -290, -32340, 0)
    ChrSetPos(0x00F9, 50160, -270, -32750, 0)
    CameraMove(49950, -200, -24790, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(2620, 0)
    OP_6C(21000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0720')
    def lambda_0720():
        ChrMoveToRelative(0x00FE, 0, 0, 5600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0720)

    Sleep(50)

    @scena.Lambda('lambda_0740')
    def lambda_0740():
        ChrMoveToRelative(0x00FE, 0, 0, 5600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_0740)

    Sleep(200)

    @scena.Lambda('lambda_0760')
    def lambda_0760():
        ChrMoveToRelative(0x00FE, 0, 0, 5500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_0760)

    Sleep(50)

    @scena.Lambda('lambda_0780')
    def lambda_0780():
        ChrMoveToRelative(0x00FE, 0, 0, 5500, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_0780)

    FadeIn(1000, 0)
    OP_0D()
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(500)

    Fade(500)
    OP_11(0xFF, 0xFF, 0xFF, 30000, 60000, 0)
    MapSetFlags(0x00000010)
    OP_12(0x00000258, 0x0000C544, 0x00000BB8)
    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#0010290881V#1000F◆哇哇……\n',
            '好浓的雾，什么都看不见。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290882V◆怎么办？雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290883V#020F◆……没办法。\n',
            '　',
            0x9,
            '只能原路返回了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_086F')
    def lambda_086F():
        ChrMoveToRelative(0x00FE, 0, 0, -5500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_086F)

    Sleep(50)

    @scena.Lambda('lambda_088F')
    def lambda_088F():
        ChrMoveToRelative(0x00FE, 0, 0, -5500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_088F)

    Sleep(100)

    @scena.Lambda('lambda_08AF')
    def lambda_08AF():
        ChrMoveToRelative(0x00FE, 0, 0, -5600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_08AF)

    Sleep(50)

    @scena.Lambda('lambda_08CF')
    def lambda_08CF():
        ChrMoveToRelative(0x00FE, 0, 0, -5600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_08CF)

    SetScenaFlags(ScenaFlag(0x0308, 1, 0x1841))
    NewScene('ED6_DT21/C0301._SN', 102, 0, 0)
    IdleLoop()

    Jump('loc_A3B')

    def _loc_8F3(): pass

    label('loc_8F3')

    ChrSetPos(0x0101, 49500, -250, -24090, 0)
    ChrSetPos(0x0103, 50640, -140, -24610, 0)
    ChrSetPos(0x00F8, 49370, -300, -25770, 0)
    ChrSetPos(0x00F9, 50600, -200, -26310, 0)
    CameraMove(49950, -200, -24790, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(2620, 0)
    OP_6C(21000, 0)
    OP_6E(262, 0)
    OP_11(0xFF, 0xFF, 0xFF, 20000, 45000, 0)
    MapSetFlags(0x00000010)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0103,
        (
            '#020F◆制雾器\n',
            '　反复的消息哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09BD')
    def lambda_09BD():
        ChrMoveToRelative(0x00FE, 0, 0, -5500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_09BD)

    Sleep(50)

    @scena.Lambda('lambda_09DD')
    def lambda_09DD():
        ChrMoveToRelative(0x00FE, 0, 0, -5500, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_09DD)

    Sleep(100)

    @scena.Lambda('lambda_09FD')
    def lambda_09FD():
        ChrMoveToRelative(0x00FE, 0, 0, -5600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_09FD)

    Sleep(50)

    @scena.Lambda('lambda_0A1D')
    def lambda_0A1D():
        ChrMoveToRelative(0x00FE, 0, 0, -5600, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_0A1D)

    NewScene('ED6_DT21/C0301._SN', 102, 0, 0)
    IdleLoop()

    def _loc_A3B(): pass

    label('loc_A3B')

    Return()

# id: 0x0004 offset: 0xA3C
@scena.Code('func_04_A3C')
def func_04_A3C():
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
        'loc_A5C',
    )

    Call(0, 0x000F)
    FadeIn(0, 0)
    Call(0, 0x0010)

    def _loc_A5C(): pass

    label('loc_A5C')

    ChrSetPos(0x0101, -49280, -190, -27370, 0)
    ChrSetPos(0x0103, -50190, -340, -27080, 0)
    ChrSetPos(0x00F8, -49390, -220, -28460, 0)
    ChrSetPos(0x00F9, -50350, -340, -28170, 0)
    CameraMove(-49490, -230, -27200, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B4B',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B89')

    def _loc_B4B(): pass

    label('loc_B4B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B72',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_B89')

    def _loc_B72(): pass

    label('loc_B72')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_B89(): pass

    label('loc_B89')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BB0',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_BEE')

    def _loc_BB0(): pass

    label('loc_BB0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_BD7',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_BEE')

    def _loc_BD7(): pass

    label('loc_BD7')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_BEE(): pass

    label('loc_BEE')

    OP_20(0x00000BB8)
    OP_12(0x00000064, 0x00002710, 0x00001770)
    Sleep(3000)

    ChrTalk(
        0x0101,
        (
            '#0010290835V#1020F#5P哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C56',
    )

    ChrTalk(
        0x0108,
        (
            '#0080290836V#072F呼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D11')

    def _loc_C56(): pass

    label('loc_C56')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C86',
    )

    ChrTalk(
        0x0106,
        (
            '#0050290837V#057F可恶……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D11')

    def _loc_C86(): pass

    label('loc_C86')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CB4',
    )

    ChrTalk(
        0x0104,
        (
            '#0040290838V#033F噢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D11')

    def _loc_CB4(): pass

    label('loc_CB4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CE2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290839V#043F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_D11')

    def _loc_CE2(): pass

    label('loc_CE2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D11',
    )

    ChrTalk(
        0x0107,
        (
            '#0070290840V#065F啊哇哇……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_D11(): pass

    label('loc_D11')

    ChrTalk(
        0x0103,
        (
            '#0030290841V#523F#6P喔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(2000)

    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C0304._SN', 100, 20, 0)
    IdleLoop()

    Return()

# id: 0x0005 offset: 0xD43
@scena.Code('func_05_D43')
def func_05_D43():
    EventBegin(0x04)
    FadeOut(0, 16777215, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D6D',
    )

    Call(0, 0x000F)
    FadeIn(0, 0)
    Call(0, 0x0010)

    def _loc_D6D(): pass

    label('loc_D6D')

    ChrSetPos(0x0101, -49280, -190, -27370, 0)
    ChrSetPos(0x0103, -50190, -340, -27080, 0)
    ChrSetPos(0x00F8, -49390, -220, -28460, 0)
    ChrSetPos(0x00F9, -50350, -340, -28170, 0)
    CameraMove(-49490, -230, -27200, 0)
    OP_67(0, 11000, -10000, 0)
    CameraSetDistance(2500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(3000, 16777215)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290888V#1025F#5P回、回来了…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290889V#022F#6P这里是……\n',
            '似乎离赛尔贝大树很近了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290890V#026F看来刚才似乎是陷入『结界』\n',
            '中了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0316, 0, 0x18B0)),
            Expr.Return,
        ),
        'loc_FF8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010290891V#1020F#5P结、结界……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290892V#1005F#5P难、难道是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290893V通往赛尔贝大树之路的消失\n',
            '也是因为……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 90, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030290894V#524F#6P呵呵……\n',
            '你也注意到了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290895V大概是结界让我们产生了幻觉，\n',
            '无法看到正确的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290896V#1020F#5P怎、怎会有这种事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_101F')

    def _loc_FF8(): pass

    label('loc_FF8')

    ChrTalk(
        0x0101,
        (
            '#0010290891V#1020F#5P结、结界……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_101F(): pass

    label('loc_101F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10E6',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1090',
    )

    ChrTalk(
        0x0108,
        (
            '#0080290898V#072F#4P也许前面\n',
            '会有机关吧，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290899V做好准备再继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10E3')

    def _loc_1090(): pass

    label('loc_1090')

    ChrTalk(
        0x0108,
        (
            '#0080290900V#072F#2P也许前面\n',
            '会有机关吧，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080290899V做好准备再继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10E3(): pass

    label('loc_10E3')

    Jump('loc_1368')

    def _loc_10E6(): pass

    label('loc_10E6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_11AD',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1157',
    )

    ChrTalk(
        0x0106,
        (
            '#0050290902V#057F#4P大概前面\n',
            '还会有机关。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290903V做好准备再继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11AA')

    def _loc_1157(): pass

    label('loc_1157')

    ChrTalk(
        0x0106,
        (
            '#0050290904V#057F#2P大概前面\n',
            '还会有机关。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290903V做好准备再继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11AA(): pass

    label('loc_11AA')

    Jump('loc_1368')

    def _loc_11AD(): pass

    label('loc_11AD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1270',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_121C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040290906V#032F#4P也许前面\n',
            '会有机关，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290907V做好准备再继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_126D')

    def _loc_121C(): pass

    label('loc_121C')

    ChrTalk(
        0x0104,
        (
            '#0040290908V#032F#2P也许前面\n',
            '会有机关，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290907V做好准备再继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_126D(): pass

    label('loc_126D')

    Jump('loc_1368')

    def _loc_1270(): pass

    label('loc_1270')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1368',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12FB',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290910V#042F#4P如果不出所料的话，前面\n',
            '也许会有机关也说不定，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290911V做好准备之后继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1368')

    def _loc_12FB(): pass

    label('loc_12FB')

    ChrTalk(
        0x0105,
        (
            '#0060290912V#042F#2P如果不出所料的话，前面\n',
            '也许会有机关也说不定，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290911V做好准备之后继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1368(): pass

    label('loc_1368')

    SetScenaFlags(ScenaFlag(0x0304, 7, 0x1827))
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x136E
@scena.Code('func_06_136E')
def func_06_136E():
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
        'loc_1397',
    )

    Call(0, 0x000F)
    FadeIn(0, 0)
    Call(0, 0x0010)
    FadeIn(0, 0)

    def _loc_1397(): pass

    label('loc_1397')

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    OP_20(0x000007D0)

    @scena.Lambda('lambda_13BE')
    def lambda_13BE():
        CameraMove(-44910, 50, 22880, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13BE)

    @scena.Lambda('lambda_13D6')
    def lambda_13D6():
        OP_67(0, 6000, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_13D6)

    @scena.Lambda('lambda_13EE')
    def lambda_13EE():
        OP_6C(27000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_13EE)

    OP_6E(189, 6000)
    Fade(500)
    ChrSetPos(0x0101, -47410, 40, 12900, 0)
    ChrSetPos(0x0103, -46420, 0, 12900, 0)
    ChrSetPos(0x00F8, -47480, -60, 11600, 0)
    ChrSetPos(0x00F9, -46420, -60, 11600, 0)
    CameraMove(-46210, -40, 15430, 0)
    OP_67(0, 6510, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290914V#1020F#6P啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290915V#022F#4P果然是『福音』……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1546',
    )

    ChrTalk(
        0x0107,
        (
            '#0070290916V#065F#4P从水面上升起的雾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070290917V也许那些雾就是在这里\n',
            '产生的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_168D')

    def _loc_1546(): pass

    label('loc_1546')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15B2',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290918V#043F#4P水面上冒着雾气……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060290919V说不定那些雾就是在这里\n',
            '产生的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_168D')

    def _loc_15B2(): pass

    label('loc_15B2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1622',
    )

    ChrTalk(
        0x0104,
        (
            '#0040290920V#032F#4P水面上冒着雾气……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290921V原来如此，那些雾就是在这里\n',
            '产生的啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_168D')

    def _loc_1622(): pass

    label('loc_1622')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_168D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050290922V#057F#4P水面上冒着雾气……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290923V难道说…那些雾就是在这里\n',
            '产生的吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_168D(): pass

    label('loc_168D')

    ChrTalk(
        0x0101,
        (
            '#0010290924V#1005F#6P那、那样的话\n',
            '我们就赶快把『福音』取下来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290925V#024F#4P艾丝蒂尔！慢着！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010270406V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_172C')
    def lambda_172C():
        CameraMove(-46100, -20, 16980, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_172C)

    @scena.Lambda('lambda_1744')
    def lambda_1744():
        OP_67(0, 5380, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1744)

    @scena.Lambda('lambda_175C')
    def lambda_175C():
        CameraSetDistance(2950, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_175C)

    @scena.Lambda('lambda_176C')
    def lambda_176C():
        OP_6C(33000, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_176C)

    @scena.Lambda('lambda_177C')
    def lambda_177C():
        OP_6E(299, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_177C)

    PlaySE(529, 0x00, 0x64)
    LoadEffect(0x00, 'scraft\\sc040_08.eff')
    PlayEffect(0x00, 0x00, 0x00FF, -46660, 1000, 19260, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    ChrSetSubChip(0x0101, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290927V#1020F#6P哇啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)
    Fade(500)
    StopEffect(0x00, 0x02)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0009, 255, 255, 255, 0, 0)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0009, 0x0004)
    ChrSetPos(0x0008, -49000, 1200, 16600, 180)
    ChrSetPos(0x0009, -45910, 1200, 16600, 180)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_1870')
    def lambda_1870():
        ChrMoveTo(0x00FE, -49000, 700, 16600, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1870)

    @scena.Lambda('lambda_188B')
    def lambda_188B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_188B)

    Sleep(800)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_18AC')
    def lambda_18AC():
        ChrMoveTo(0x00FE, -45910, 600, 16600, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_18AC)

    @scena.Lambda('lambda_18C7')
    def lambda_18C7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_18C7)

    Sleep(800)

    PlaySE(538, 0x00, 0x64)
    Sleep(800)

    PlaySE(538, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1941',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_197F')

    def _loc_1941(): pass

    label('loc_1941')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1968',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_197F')

    def _loc_1968(): pass

    label('loc_1968')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_197F(): pass

    label('loc_197F')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19A6',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_19E4')

    def _loc_19A6(): pass

    label('loc_19A6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_19CD',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_19E4')

    def _loc_19CD(): pass

    label('loc_19CD')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_19E4(): pass

    label('loc_19E4')

    Sleep(500)

    PlayBGM(41)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290928V#1020F#6P这、这些是什么东西！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290929V#022F#4P这两只怪物似乎比我们在\n',
            '农场打倒的那些强得多……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 12)
    ChrSetSubChip(0x0101, 0)
    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0103, 16)
    ChrSetSubChip(0x0103, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AB6',
    )

    Sleep(50)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0104, 22)
    ChrSetSubChip(0x0104, 0)

    Jump('loc_1B43')

    def _loc_1AB6(): pass

    label('loc_1AB6')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1ADA',
    )

    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0105, 20)
    ChrSetSubChip(0x0105, 0)

    Jump('loc_1B43')

    def _loc_1ADA(): pass

    label('loc_1ADA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1AFE',
    )

    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0108, 24)
    ChrSetSubChip(0x0108, 0)

    Jump('loc_1B43')

    def _loc_1AFE(): pass

    label('loc_1AFE')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B22',
    )

    Sleep(50)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0107, 18)
    ChrSetSubChip(0x0107, 0)

    Jump('loc_1B43')

    def _loc_1B22(): pass

    label('loc_1B22')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B43',
    )

    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0106, 14)
    ChrSetSubChip(0x0106, 0)

    def _loc_1B43(): pass

    label('loc_1B43')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B67',
    )

    Sleep(50)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0104, 22)
    ChrSetSubChip(0x0104, 0)

    Jump('loc_1BF4')

    def _loc_1B67(): pass

    label('loc_1B67')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1B8B',
    )

    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0105, 20)
    ChrSetSubChip(0x0105, 0)

    Jump('loc_1BF4')

    def _loc_1B8B(): pass

    label('loc_1B8B')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BAF',
    )

    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0108, 24)
    ChrSetSubChip(0x0108, 0)

    Jump('loc_1BF4')

    def _loc_1BAF(): pass

    label('loc_1BAF')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BD3',
    )

    Sleep(50)

    PlaySE(216, 0x00, 0x64)
    ChrSetChipByIndex(0x0107, 18)
    ChrSetSubChip(0x0107, 0)

    Jump('loc_1BF4')

    def _loc_1BD3(): pass

    label('loc_1BD3')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BF4',
    )

    Sleep(50)

    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0106, 14)
    ChrSetSubChip(0x0106, 0)

    def _loc_1BF4(): pass

    label('loc_1BF4')

    OP_0D()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C2E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050290930V#054F#4P……它们来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD0')

    def _loc_1C2E(): pass

    label('loc_1C2E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C63',
    )

    ChrTalk(
        0x0108,
        (
            '#0080290931V#076F#4P……来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD0')

    def _loc_1C63(): pass

    label('loc_1C63')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C9C',
    )

    ChrTalk(
        0x0105,
        (
            '#0060290932V#042F#4P……它们来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1CD0')

    def _loc_1C9C(): pass

    label('loc_1C9C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CD0',
    )

    ChrTalk(
        0x0104,
        (
            '#0040290933V#032F#4P……要来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1CD0(): pass

    label('loc_1CD0')

    Sleep(500)

    @scena.Lambda('lambda_1CDB')
    def lambda_1CDB():
        CameraMove(-45350, -50, 14500, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1CDB)

    @scena.Lambda('lambda_1CF3')
    def lambda_1CF3():
        CameraSetDistance(2680, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1CF3)

    ChrSetChipByIndex(0x0008, 27)

    @scena.Lambda('lambda_1D08')
    def lambda_1D08():
        ChrWalkTo(0x00FE, -47810, 200, 13200, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_1D08)

    Sleep(50)

    ChrSetChipByIndex(0x0009, 26)

    @scena.Lambda('lambda_1D2D')
    def lambda_1D2D():
        ChrWalkTo(0x00FE, -45890, 200, 12850, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1D2D)

    Sleep(200)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0103, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x0009, 0xFF)
    Battle(0x0000045F, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_1D78'),
        (-1, 'loc_1D7D'),
    )

    def _loc_1D78(): pass

    label('loc_1D78')

    OP_B4(0x00)

    Jump('loc_1D7D')

    def _loc_1D7D(): pass

    label('loc_1D7D')

    Call(0, 0x0007)

    Return()

# id: 0x0007 offset: 0x1D82
@scena.Code('func_07_1D82')
def func_07_1D82():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, -47410, 40, 12950, 0)
    ChrSetPos(0x0103, -46420, 0, 12860, 0)
    ChrSetPos(0x00F8, -47480, -60, 11470, 0)
    ChrSetPos(0x00F9, -46420, -60, 11450, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    ChrSetPos(0x0101, -47410, 40, 12900, 0)
    ChrSetPos(0x0103, -46420, 0, 12900, 0)
    ChrSetPos(0x00F8, -47480, -60, 11600, 0)
    ChrSetPos(0x00F9, -46420, -60, 11600, 0)
    CameraMove(-46210, -40, 15430, 0)
    OP_67(0, 6510, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010290934V#1007F#6P呼、呼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290935V#1019F真、真没想到竟然\n',
            '会这么难缠……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290936V#024F#4P不要大意啊！\n',
            '刚才我们打倒的只是召唤出来的妖物！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290937V操纵它们的施术者\n',
            '应该还藏在附近！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290938V#1004F#6P什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0210290939V呵呵……\n',
            '你们还挺努力的嘛，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0210290940V既然如此的话我就\n',
            '奖励你们一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)

    ChrTalk(
        0x0103,
        (
            '#0030290941V#022F#4P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    OP_20(0x000007D0)

    @scena.Lambda('lambda_2040')
    def lambda_2040():
        CameraMove(-45170, 20, 19670, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2040)

    @scena.Lambda('lambda_2058')
    def lambda_2058():
        OP_67(0, 5380, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2058)

    @scena.Lambda('lambda_2070')
    def lambda_2070():
        CameraSetDistance(2950, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2070)

    @scena.Lambda('lambda_2080')
    def lambda_2080():
        OP_6C(33000, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2080)

    @scena.Lambda('lambda_2090')
    def lambda_2090():
        OP_6E(299, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_2090)

    Sleep(2500)

    LoadEffect(0x00, 'map\\\\mp007_00.eff')
    WaitForThreadExit(0x0101, 0x0001)
    PlayBGM(92)
    Sleep(1000)

    PlaySE(144, 0x00, 0x64)
    PlayEffect(0x00, 0xFF, 0x00FF, -46500, 2800, 19600, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(2000)

    ChrTalk(
        0x0101,
        (
            '#0010290942V#1020F#5P什…什么…！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030290943V#523F#2P糟了……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_C0(0x14, 0x00001388, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000)
    OP_20(0x00001388)
    OP_24(0x0090, 0x5A)
    Sleep(400)

    OP_24(0x0090, 0x50)
    Sleep(400)

    OP_24(0x0090, 0x46)
    Sleep(400)

    OP_24(0x0090, 0x3C)
    Sleep(400)

    OP_24(0x0090, 0x32)
    Sleep(400)

    OP_24(0x0090, 0x28)
    Sleep(400)

    OP_24(0x0090, 0x1E)
    Sleep(400)

    OP_24(0x0090, 0x14)
    Sleep(400)

    OP_23(0x0090)
    OP_0D()
    Sleep(1000)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_21E7'),
        (0x00000006, 'loc_21ED'),
        (0x00000003, 'loc_21F3'),
        (0x00000004, 'loc_21F9'),
        (0x00000007, 'loc_21FF'),
        (-1, 'loc_2205'),
    )

    def _loc_21E7(): pass

    label('loc_21E7')

    SetScenaFlags(ScenaFlag(0x0305, 1, 0x1829))

    Jump('loc_2205')

    def _loc_21ED(): pass

    label('loc_21ED')

    SetScenaFlags(ScenaFlag(0x0305, 2, 0x182A))

    Jump('loc_2205')

    def _loc_21F3(): pass

    label('loc_21F3')

    SetScenaFlags(ScenaFlag(0x0305, 3, 0x182B))

    Jump('loc_2205')

    def _loc_21F9(): pass

    label('loc_21F9')

    SetScenaFlags(ScenaFlag(0x0305, 4, 0x182C))

    Jump('loc_2205')

    def _loc_21FF(): pass

    label('loc_21FF')

    SetScenaFlags(ScenaFlag(0x0305, 5, 0x182D))

    Jump('loc_2205')

    def _loc_2205(): pass

    label('loc_2205')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_2222'),
        (0x00000006, 'loc_2228'),
        (0x00000003, 'loc_222E'),
        (0x00000004, 'loc_2234'),
        (0x00000007, 'loc_223A'),
        (-1, 'loc_2240'),
    )

    def _loc_2222(): pass

    label('loc_2222')

    SetScenaFlags(ScenaFlag(0x0305, 6, 0x182E))

    Jump('loc_2240')

    def _loc_2228(): pass

    label('loc_2228')

    SetScenaFlags(ScenaFlag(0x0305, 7, 0x182F))

    Jump('loc_2240')

    def _loc_222E(): pass

    label('loc_222E')

    SetScenaFlags(ScenaFlag(0x0306, 0, 0x1830))

    Jump('loc_2240')

    def _loc_2234(): pass

    label('loc_2234')

    SetScenaFlags(ScenaFlag(0x0306, 1, 0x1831))

    Jump('loc_2240')

    def _loc_223A(): pass

    label('loc_223A')

    SetScenaFlags(ScenaFlag(0x0306, 2, 0x1832))

    Jump('loc_2240')

    def _loc_2240(): pass

    label('loc_2240')

    FormationReset()
    FormationAddMember(ChrTable['艾丝蒂尔'], 0xF6, 0xFF)

    OP_CE(
        0x00,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_CE(
        0x02,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetScenaFlags(ScenaFlag(0x0305, 0, 0x1828))
    OP_28(0x0092, 0x01, 0x0020)
    OP_28(0x0092, 0x01, 0x0040)
    OP_28(0x0092, 0x01, 0x0080)
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T0300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x2279
@scena.Code('func_08_2279')
def func_08_2279():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0200, 1, 0x1001)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24E3',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 1, 0x1829)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 2, 0x182A)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 3, 0x182B)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 4, 0x182C)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 5, 0x182D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_24E3',
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
        100,
        0,
        (
            TXT(0x00, '【◇队伍变成１人之前，阿加特是队员２】\n'),
            TXT(0x01, '【◇队伍变成１人之前，提妲是队员２】\n'),
            TXT(0x02, '【◇队伍变成１人之前，奥利维尔是队员２】\n'),
            TXT(0x03, '【◇队伍变成１人之前，科洛丝是队员２】\n'),
            TXT(0x04, '【◇队伍变成１人之前，金是队员２】\n'),
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
        (0x00000000, 'loc_23A8'),
        (0x00000001, 'loc_23AE'),
        (0x00000002, 'loc_23B4'),
        (0x00000003, 'loc_23BA'),
        (0x00000004, 'loc_23C0'),
        (-1, 'loc_23C6'),
    )

    def _loc_23A8(): pass

    label('loc_23A8')

    SetScenaFlags(ScenaFlag(0x0305, 1, 0x1829))

    Jump('loc_23C6')

    def _loc_23AE(): pass

    label('loc_23AE')

    SetScenaFlags(ScenaFlag(0x0305, 2, 0x182A))

    Jump('loc_23C6')

    def _loc_23B4(): pass

    label('loc_23B4')

    SetScenaFlags(ScenaFlag(0x0305, 3, 0x182B))

    Jump('loc_23C6')

    def _loc_23BA(): pass

    label('loc_23BA')

    SetScenaFlags(ScenaFlag(0x0305, 4, 0x182C))

    Jump('loc_23C6')

    def _loc_23C0(): pass

    label('loc_23C0')

    SetScenaFlags(ScenaFlag(0x0305, 5, 0x182D))

    Jump('loc_23C6')

    def _loc_23C6(): pass

    label('loc_23C6')

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
            TXT(0x00, '【◇队伍变成１人之前，阿加特是队员３】\n'),
            TXT(0x01, '【◇队伍变成１人之前，提妲是队员３】\n'),
            TXT(0x02, '【◇队伍变成１人之前，奥利维尔是队员３】\n'),
            TXT(0x03, '【◇队伍变成１人之前，科洛丝是队员３】\n'),
            TXT(0x04, '【◇队伍变成１人之前，金是队员３】\n'),
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
        (0x00000000, 'loc_24C5'),
        (0x00000001, 'loc_24CB'),
        (0x00000002, 'loc_24D1'),
        (0x00000003, 'loc_24D7'),
        (0x00000004, 'loc_24DD'),
        (-1, 'loc_24E3'),
    )

    def _loc_24C5(): pass

    label('loc_24C5')

    SetScenaFlags(ScenaFlag(0x0305, 6, 0x182E))

    Jump('loc_24E3')

    def _loc_24CB(): pass

    label('loc_24CB')

    SetScenaFlags(ScenaFlag(0x0305, 7, 0x182F))

    Jump('loc_24E3')

    def _loc_24D1(): pass

    label('loc_24D1')

    SetScenaFlags(ScenaFlag(0x0306, 0, 0x1830))

    Jump('loc_24E3')

    def _loc_24D7(): pass

    label('loc_24D7')

    SetScenaFlags(ScenaFlag(0x0306, 1, 0x1831))

    Jump('loc_24E3')

    def _loc_24DD(): pass

    label('loc_24DD')

    SetScenaFlags(ScenaFlag(0x0306, 2, 0x1832))

    Jump('loc_24E3')

    def _loc_24E3(): pass

    label('loc_24E3')

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 1, 0x1829)),
            Expr.Return,
        ),
        'loc_24F5',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF8, 0xFF)

    Jump('loc_252A')

    def _loc_24F5(): pass

    label('loc_24F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 2, 0x182A)),
            Expr.Return,
        ),
        'loc_2503',
    )

    FormationAddMember(ChrTable['提妲'], 0xF8, 0xFF)

    Jump('loc_252A')

    def _loc_2503(): pass

    label('loc_2503')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 3, 0x182B)),
            Expr.Return,
        ),
        'loc_2511',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xF8, 0xFF)

    Jump('loc_252A')

    def _loc_2511(): pass

    label('loc_2511')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 4, 0x182C)),
            Expr.Return,
        ),
        'loc_251F',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xF8, 0xFF)

    Jump('loc_252A')

    def _loc_251F(): pass

    label('loc_251F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 5, 0x182D)),
            Expr.Return,
        ),
        'loc_252A',
    )

    FormationAddMember(ChrTable['金'], 0xF8, 0xFF)

    def _loc_252A(): pass

    label('loc_252A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 6, 0x182E)),
            Expr.Return,
        ),
        'loc_2538',
    )

    FormationAddMember(ChrTable['阿加特'], 0xF9, 0xFF)

    Jump('loc_256D')

    def _loc_2538(): pass

    label('loc_2538')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0305, 7, 0x182F)),
            Expr.Return,
        ),
        'loc_2546',
    )

    FormationAddMember(ChrTable['提妲'], 0xF9, 0xFF)

    Jump('loc_256D')

    def _loc_2546(): pass

    label('loc_2546')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 0, 0x1830)),
            Expr.Return,
        ),
        'loc_2554',
    )

    FormationAddMember(ChrTable['奥利维尔'], 0xF9, 0xFF)

    Jump('loc_256D')

    def _loc_2554(): pass

    label('loc_2554')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 1, 0x1831)),
            Expr.Return,
        ),
        'loc_2562',
    )

    FormationAddMember(ChrTable['科洛丝'], 0xF9, 0xFF)

    Jump('loc_256D')

    def _loc_2562(): pass

    label('loc_2562')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0306, 2, 0x1832)),
            Expr.Return,
        ),
        'loc_256D',
    )

    FormationAddMember(ChrTable['金'], 0xF9, 0xFF)

    def _loc_256D(): pass

    label('loc_256D')

    CameraMove(-46680, 20, 12540, 0)
    OP_67(0, 6420, -10000, 0)
    CameraSetDistance(2960, 0)
    OP_6C(45000, 0)
    OP_6E(299, 0)
    ChrSetPos(0x0101, -47720, 20, 12910, 0)
    ChrSetPos(0x0103, -46230, -20, 13170, 270)
    ChrSetPos(0x00F8, -47480, -60, 11470, 0)
    ChrSetPos(0x00F9, -46420, -60, 11450, 0)

    NpcTalk(
        0x0103,
        '女性的声音',
        (
            '#0030291300V#2P艾丝蒂尔！\n',
            '振作一点啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291301V#1007F#6P嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetChipByIndex(0x0101, 3)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_2668'),
        (0x00000006, 'loc_2670'),
        (0x00000003, 'loc_2678'),
        (0x00000004, 'loc_2680'),
        (0x00000007, 'loc_2688'),
        (-1, 'loc_2690'),
    )

    def _loc_2668(): pass

    label('loc_2668')

    ChrSetChipByIndex(0x00F8, 4)

    Jump('loc_2690')

    def _loc_2670(): pass

    label('loc_2670')

    ChrSetChipByIndex(0x00F8, 5)

    Jump('loc_2690')

    def _loc_2678(): pass

    label('loc_2678')

    ChrSetChipByIndex(0x00F8, 6)

    Jump('loc_2690')

    def _loc_2680(): pass

    label('loc_2680')

    ChrSetChipByIndex(0x00F8, 7)

    Jump('loc_2690')

    def _loc_2688(): pass

    label('loc_2688')

    ChrSetChipByIndex(0x00F8, 8)

    Jump('loc_2690')

    def _loc_2690(): pass

    label('loc_2690')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_26AD'),
        (0x00000006, 'loc_26B5'),
        (0x00000003, 'loc_26BD'),
        (0x00000004, 'loc_26C5'),
        (0x00000007, 'loc_26CD'),
        (-1, 'loc_26D5'),
    )

    def _loc_26AD(): pass

    label('loc_26AD')

    ChrSetChipByIndex(0x00F9, 4)

    Jump('loc_26D5')

    def _loc_26B5(): pass

    label('loc_26B5')

    ChrSetChipByIndex(0x00F9, 5)

    Jump('loc_26D5')

    def _loc_26BD(): pass

    label('loc_26BD')

    ChrSetChipByIndex(0x00F9, 6)

    Jump('loc_26D5')

    def _loc_26C5(): pass

    label('loc_26C5')

    ChrSetChipByIndex(0x00F9, 7)

    Jump('loc_26D5')

    def _loc_26CD(): pass

    label('loc_26CD')

    ChrSetChipByIndex(0x00F9, 8)

    Jump('loc_26D5')

    def _loc_26D5(): pass

    label('loc_26D5')

    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291302V#1026F#6P啊……雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291303V#023F#2P艾丝蒂尔！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291304V#524F太好了……\n',
            '你终于醒过来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291305V#1025F#6P啊……嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291306V我好像…\n',
            '做了一个好长好长的梦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    ChrSetDirection(0x0101, 180, 400)
    Sleep(500)

    Fade(1000)
    ChrSetChipByIndex(0x0101, 9)
    ChrSetSubChip(0x0101, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291307V#1017F#5P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291308V……多亏了它……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291309V#1005F#5P你们两个！！\n',
            '美梦已经结束了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291310V赶快回到现实来！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291311V#023F#2P艾、艾丝蒂尔！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_28FF',
    )

    ChrTalk(
        0x0107,
        (
            '#0070291312V#561F嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B6')

    def _loc_28FF(): pass

    label('loc_28FF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_292D',
    )

    ChrTalk(
        0x0106,
        (
            '#0050291313V#056F厄……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B6')

    def _loc_292D(): pass

    label('loc_292D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_295D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040291314V#034F嗯啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B6')

    def _loc_295D(): pass

    label('loc_295D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_298B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060291315V#049F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B6')

    def _loc_298B(): pass

    label('loc_298B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_29B6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080291316V#572F呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29B6(): pass

    label('loc_29B6')

    OP_9E(0x00F8, 15, 0, 300, 4000)
    Fade(500)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetSubChip(0x00F8, 0)
    OP_0D()
    Sleep(500)

    OP_9E(0x00F9, 15, 0, 300, 4000)
    Fade(500)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x00F9, 0)
    OP_0D()
    Sleep(500)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A44',
    )

    ChrTalk(
        0x0107,
        (
            '#0070291317V#064F啊……艾丝蒂尔姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AED')

    def _loc_2A44(): pass

    label('loc_2A44')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2A7E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060291318V#044F啊……艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AED')

    def _loc_2A7E(): pass

    label('loc_2A7E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2ABA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040291319V#033F哎呀……艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2AED')

    def _loc_2ABA(): pass

    label('loc_2ABA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2AED',
    )

    ChrTalk(
        0x0106,
        (
            '#0050291320V#052F艾丝蒂尔……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2AED(): pass

    label('loc_2AED')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B32',
    )

    ChrTalk(
        0x0108,
        (
            '#0080291321V#572F是吗……\n',
            '原来被困在梦中了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BFC')

    def _loc_2B32(): pass

    label('loc_2B32')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2B7B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050291322V#552F是吗……\n',
            '原来刚才的一切都是梦啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BFC')

    def _loc_2B7B(): pass

    label('loc_2B7B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BBE',
    )

    ChrTalk(
        0x0104,
        (
            '#0040291323V#032F嗯……\n',
            '原来被困在梦中了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2BFC')

    def _loc_2BBE(): pass

    label('loc_2BBE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2BFC',
    )

    ChrTalk(
        0x0105,
        (
            '#0060291324V#049F是吗……\n',
            '原来…是梦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2BFC(): pass

    label('loc_2BFC')

    ChrTalk(
        0x0101,
        (
            '#0010291325V#1006F#5P太好了……\n',
            '大家都醒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291326V#524F#2P呵……\n',
            '都是被艾丝蒂尔你吓醒的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291327V不但可以凭自己的力量醒来，\n',
            '竟然还能把别人也叫醒呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291328V#026F那么，接下来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 0, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030291329V#024F#2P#3S你在这里吧？快现身吧！\n',
            '露茜奥拉姐姐！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010291330V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('女性的声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0210291331V呵呵……\n',
            '终于被认出来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    PlayBGM(111)
    Sleep(300)

    @scena.Lambda('lambda_2DCB')
    def lambda_2DCB():
        CameraMove(-45560, -10, 16980, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2DCB)

    @scena.Lambda('lambda_2DE3')
    def lambda_2DE3():
        OP_67(0, 5240, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2DE3)

    @scena.Lambda('lambda_2DFB')
    def lambda_2DFB():
        OP_6C(45000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2DFB)

    @scena.Lambda('lambda_2E0B')
    def lambda_2E0B():
        OP_6E(325, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2E0B)

    @scena.Lambda('lambda_2E1B')
    def lambda_2E1B():
        CameraSetDistance(2950, 3000)

        ExitThread()

    DispatchAsync(0x0103, 0x0002, lambda_2E1B)

    ChrSetDirection(0x0101, 0, 400)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetPos(0x000C, -46320, 70, 19130, 180)

    @scena.Lambda('lambda_2E5D')
    def lambda_2E5D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1500)

        ExitThread()

    DispatchAsync(0x000C, 0x0000, lambda_2E5D)

    PlaySE(153, 0x00, 0x64)
    CreateThread(0x000A, 0x01, 0x00, func_0A_40B8)
    CreateThread(0x000B, 0x01, 0x00, func_0B_41A1)
    StopEffect(0x00, 0x02)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EBD',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2EFB')

    def _loc_2EBD(): pass

    label('loc_2EBD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2EE4',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2EFB')

    def _loc_2EE4(): pass

    label('loc_2EE4')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_2EFB(): pass

    label('loc_2EFB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F22',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2F60')

    def _loc_2F22(): pass

    label('loc_2F22')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2F49',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2F60')

    def _loc_2F49(): pass

    label('loc_2F49')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_2F60(): pass

    label('loc_2F60')

    Sleep(1000)

    WaitForThreadExit(0x000C, 0x0001)
    WaitForThreadExit(0x000A, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010291332V#1020F#6P什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291333V#022F#2P……果然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '黑衣女子',
        (
            '#0210291334V#240F好久不见了啊，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291335V已经有８年了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291336V#522F#2P嗯……是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291337V真没想到姐姐你竟然…\n',
            '会做出这样的事情来……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291338V#022F你究竟、为什么要这么做！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrSetDirection(0x0101, 90, 500)
    Sleep(500)

    ChrSetDirection(0x0101, 0, 500)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010261066V#1020F#6P等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291340V这个人……\n',
            '和雪拉姐是旧识吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '黑衣女子',
        (
            '#0210291341V#241F呵呵……\n',
            '真是薄情啊，小鬼头。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291342V你我之间可也是\n',
            '见过好几次面的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010261072V#1004F#6P哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '黑衣女子',
        (
            '#0210291344V#241F和你一起玩塔罗牌\n',
            '的幻术师姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291345V你已经不记得了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291346V#1020F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT24/C_VIS102._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    OP_AE(0x000001F4)
    Sleep(1500)

    ChrTalk(
        0x0101,
        (
            '#0010291347V#1020F#6P你、你就是当时的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291348V露……\n',
            '露茜奥拉姐姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '黑衣女子',
        (
            '#0210291349V#241F呵呵～没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_C5(0x00, 0, 0, 512, 512, 100, 0, 768, 512, 0, 0, 512, 512, 0x00FFFFFF, 0x00, 'C_VIS117._CH')
    OP_C6(0x00, 0x00, 125000, 0, 500)
    OP_C6(0x00, 0x03, -1, 500, 0)
    Sleep(1000)

    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('黑衣女子')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '#0210291350V#241F执行者ＮＯ．Ⅵ。\n',
            '『幻惑之铃』露茜奥拉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291351V这就是我现在的名字哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_C6(0x00, 0x03, 16777215, 250, 0)
    Sleep(250)

    OP_C6(0x00, 0x06, 0, 0, 0)

    ChrTalk(
        0x0101,
        (
            '#0010291352V#1020F#6P为、为什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291353V#240F呵呵、雪拉扎德。\n',
            '你似乎早就猜出是我了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291354V#026F#2P驱铃之幻术……\n',
            '可是姐姐的拿手绝活啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291355V#022F不过洛连特产生的浓雾\n',
            '应该不是用幻术做出的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291356V#241F呵呵，当然。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291357V那个是为了这次的实验\n',
            '而用『福音』引起的现象哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291358V能顺利干涉到人们的梦境，\n',
            '这些雾可是起到了重要的触媒作用哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291359V#023F#2P触媒……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291360V#024F难道说『福音』\n',
            '连人的精神也可以干扰到吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291361V#240F呵呵～似乎就是这样哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291362V我的铃声只是诱导……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291363V诱导大家进入远比幻术\n',
            '还要真实的梦境。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291364V#244F在梦境里，大家没有痛苦，\n',
            '没有悲伤，只有幸福和快乐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_369D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070291365V#063F怎、怎么会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_369D(): pass

    label('loc_369D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36D7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050291366V#552F可恶……\n',
            '竟敢耍我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36D7(): pass

    label('loc_36D7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3719',
    )

    ChrTalk(
        0x0104,
        (
            '#0040291367V#032F哎呀呀……\n',
            '真是低级的嗜好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3719(): pass

    label('loc_3719')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3752',
    )

    ChrTalk(
        0x0105,
        (
            '#0060291368V#043F…………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3752(): pass

    label('loc_3752')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3789',
    )

    ChrTalk(
        0x0108,
        (
            '#0080291369V#072F嗯、原来如此啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3789(): pass

    label('loc_3789')

    ChrTalk(
        0x0103,
        (
            '#0030291370V#522F#2P……呜………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291371V#1002F#6P那个、露茜奥拉……姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291372V为什么『结社』\n',
            '要一直干这种事？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291373V不断进行这些实验，\n',
            '到底是为了什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291374V#240F我身为结社的『执行者』，\n',
            '只会按照『使徒』的指示而行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291375V也就是说，我只不过是\n',
            '这次计划的协力者而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291376V详细情况\n',
            '你们就去问教授和莱维吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291377V#1002F#6P教授、莱维……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010291378V这两个名字我们已经听过好几次了，\n',
            '他们究竟是谁呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291379V#241F时候一到，你们自然就知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291380V顺便一提，他们两个\n',
            '好像都认识你呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291381V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291382V#522F#2P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291383V……露茜奥拉姐姐。\n',
            '你能听我说几句话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291384V#243F啊……是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    OP_21()
    PlayBGM(83)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030291385V#524F#2P在一开始，我并没有打算\n',
            '定居在利贝尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291386V只是想在姐姐回来之前\n',
            '暂时待在这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291387V#026F可是，８年时间转眼就过去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291388V现在的我，在这里已经有了朋友和同伴，\n',
            '有了相当于家人一般的人们，\n',
            '也有了引以为荣的工作。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291389V#022F我早已经……不再是哈维剧团里\n',
            '那个跳舞的小孩雪拉扎德了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291390V#1026F#6P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291391V#242F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291392V#026F#2P这里是我新的家乡……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0103, 16)
    ChrSetSubChip(0x0103, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030291393V#024F#2P如果有人想破坏这里的话，\n',
            '就算是姐姐你我也不会原谅的！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291394V#244F呵呵……很好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291395V#241F对你们来说，\n',
            '『结社』实在是太过强大了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291396V想要与之抗衡，就要拿出全部的力量。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    Fade(1000)
    OP_71(0x0000, 0x0004)
    PlaySE(130, 0x00, 0x64)
    OP_0D()
    CreateThread(0x000A, 0x01, 0x00, func_0C_428A)
    CreateThread(0x000B, 0x01, 0x00, func_0D_4335)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0003, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010291397V#1004F#6P啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030291398V#023F#2P姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0210291399V#241F呵呵……\n',
            '不久之后我们还会再见面的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210291400V想叙旧的话到时候再继续吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(286, 0x00, 0x64)

    @scena.Lambda('lambda_3EA7')
    def lambda_3EA7():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

        ExitThread()

    DispatchAsync(0x000C, 0x0002, lambda_3EA7)

    @scena.Lambda('lambda_3EB9')
    def lambda_3EB9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_3EB9)

    @scena.Lambda('lambda_3ECB')
    def lambda_3ECB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_3ECB)

    Sleep(500)

    @scena.Lambda('lambda_3EE2')
    def lambda_3EE2():
        CameraMove(-45830, 10, 17150, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3EE2)

    @scena.Lambda('lambda_3EFA')
    def lambda_3EFA():
        OP_6C(33000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3EFA)

    ChrSetChipByIndex(0x0103, 65535)
    ChrWalkTo(0x0103, -46630, 20, 17110, 5000, 0x00)
    WaitForThreadExit(0x000C, 0x0002)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x000B, 0xFF)
    WaitForThreadExit(0x0101, 0x0000)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030291401V#522F#5P……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010291390V#1026F#6P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030291403V#025F#6P……呼，真是的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 180, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030291404V#524F#5P虽然被她逃走了……\n',
            '但事件至此为止应该也算是解决了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030291405V昏睡中的人们\n',
            '应该马上都会醒来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    NewScene('ED6_DT21/T0100._SN', 119, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x406C
@scena.Code('func_09_406C')
def func_09_406C():
    OP_24(0x010A, 0x5A)
    Sleep(100)

    OP_24(0x010A, 0x50)
    Sleep(100)

    OP_24(0x010A, 0x46)
    Sleep(100)

    OP_24(0x010A, 0x3C)
    Sleep(100)

    OP_24(0x010A, 0x32)
    Sleep(100)

    OP_24(0x010A, 0x28)
    Sleep(100)

    OP_24(0x010A, 0x1E)
    Sleep(100)

    OP_24(0x010A, 0x14)
    Sleep(100)

    OP_23(0x010A)

    Return()

# id: 0x000A offset: 0x40B8
@scena.Code('func_0A_40B8')
def func_0A_40B8():
    ChrSetSubChip(0x000A, 0)
    ChrSetPos(0x000A, -46320, 70, 19130, 180)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_40DF')
    def lambda_40DF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 90, 500)

        ExitThread()

    DispatchAsync(0x000A, 0x0003, lambda_40DF)

    ChrClearFlags(0x000A, 0x0080)
    ChrMoveToRelativeAsync(0x000A, 150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, -150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, 150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, -150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, 100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, -100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, 50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, -50, 0, 0, 300, 0x00)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 0, 500)
    ChrSetFlags(0x000A, 0x0080)

    Return()

# id: 0x000B offset: 0x41A1
@scena.Code('func_0B_41A1')
def func_0B_41A1():
    ChrSetSubChip(0x000B, 0)
    ChrSetPos(0x000B, -46320, 70, 19130, 180)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_41C8')
    def lambda_41C8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 90, 500)

        ExitThread()

    DispatchAsync(0x000B, 0x0003, lambda_41C8)

    ChrClearFlags(0x000B, 0x0080)
    ChrMoveToRelativeAsync(0x000B, -150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, 150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, -150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, 150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, -100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, 100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, -50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, 50, 0, 0, 300, 0x00)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 0, 500)
    ChrSetFlags(0x000B, 0x0080)

    Return()

# id: 0x000C offset: 0x428A
@scena.Code('func_0C_428A')
def func_0C_428A():
    ChrSetSubChip(0x000A, 0)
    ChrSetPos(0x000A, -46320, 70, 19130, 180)
    ChrSetRGBAMask(0x000A, 255, 255, 255, 90, 0)
    ChrClearFlags(0x000A, 0x0080)
    ChrMoveToRelativeAsync(0x000A, 50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, -50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, 100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, -100, 0, 0, 300, 0x00)
    def _loc_4300(): pass

    label('loc_4300')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_4334',
    )

    ChrMoveToRelativeAsync(0x000A, 150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000A, -150, 0, 0, 300, 0x00)

    Jump('loc_4300')

    def _loc_4334(): pass

    label('loc_4334')

    Return()

# id: 0x000D offset: 0x4335
@scena.Code('func_0D_4335')
def func_0D_4335():
    ChrSetSubChip(0x000B, 0)
    ChrSetPos(0x000B, -46320, 70, 19130, 180)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 90, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrMoveToRelativeAsync(0x000B, -50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, 50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, -100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, 100, 0, 0, 300, 0x00)
    def _loc_43AB(): pass

    label('loc_43AB')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_43DF',
    )

    ChrMoveToRelativeAsync(0x000B, -150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, 150, 0, 0, 300, 0x00)

    Jump('loc_43AB')

    def _loc_43DF(): pass

    label('loc_43DF')

    Return()

# id: 0x000E offset: 0x43E0
@scena.Code('func_0E_43E0')
def func_0E_43E0():
    EventBegin(0x01)

    ChrTalk(
        0x0101,
        (
            '#0011860001V#1001F这里好像可以钓上什么来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_4418')
    def lambda_4418():
        CameraMove(55440, 360, 7980, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_4418)

    @scena.Lambda('lambda_4430')
    def lambda_4430():
        CameraSetDistance(3200, 1500)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_4430)

    Sleep(1000)

    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼吗？',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
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
        32,
        1,
        (
            TXT(0x00, '钓鱼\n'),
            TXT(0x01, '离开\n'),
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
    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0000, 0x0002)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4568',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.Eval, "OP_C0(0x0E, 0x00000003, 0x0000D174, 0x0000017C, 0x00002044, 0x0000005A, 0x0000DEC6, 0xFFFFFC18, 0x00001E32)"),
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        'loc_4562',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x08)"),
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0073, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_455C',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0073, 0x01, 0x0040)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4559',
    )

    OP_28(0x0073, 0x01, 0x0002)
    OP_28(0x0073, 0x01, 0x0040)
    Sleep(400)

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把在神秘森林中发现钓鱼场的事情\n',
            '已经记录在游击士手册上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    def _loc_4559(): pass

    label('loc_4559')

    Jump('loc_4562')

    def _loc_455C(): pass

    label('loc_455C')

    OP_28(0x0073, 0x01, 0x4000)

    def _loc_4562(): pass

    label('loc_4562')

    OP_0D()
    EventEnd(0x01)

    Jump('loc_4577')

    def _loc_4568(): pass

    label('loc_4568')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4577',
    )

    EventEnd(0x01)

    def _loc_4577(): pass

    label('loc_4577')

    Return()

# id: 0x000F offset: 0x4578
@scena.Code('func_0F_4578')
def func_0F_4578():
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
        (0x00000000, 'loc_45F5'),
        (0x00000001, 'loc_45FB'),
        (-1, 'loc_4601'),
    )

    def _loc_45F5(): pass

    label('loc_45F5')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_4601')

    def _loc_45FB(): pass

    label('loc_45FB')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_4601')

    def _loc_4601(): pass

    label('loc_4601')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_460F',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_4613')

    def _loc_460F(): pass

    label('loc_460F')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_4613(): pass

    label('loc_4613')

    Return()

# id: 0x0010 offset: 0x4614
@scena.Code('func_10_4614')
def func_10_4614():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
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

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
