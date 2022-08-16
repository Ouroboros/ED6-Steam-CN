import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5308_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5308   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5308.x'
    header.mapIndex       = 1
    header.bgm            = 64
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
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '怪盗布卢布兰',
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
            name                = '跳梁小丑',
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
            name                = '跳梁小丑',
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
            name                = '目标用照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x128
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x128
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x128
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = 32500,
            triggerRange        = 800,
            actorX              = 0,
            actorZ              = 1000,
            actorY              = 32500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x14C
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_15D',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_12_3722)

    Jump('loc_177')

    def _loc_15D(): pass

    label('loc_15D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 2, 0x2232)),
            Expr.Ez,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_177',
    )

    MapSetFlags(0x10000000)
    Event(0, func_03_3A6)

    def _loc_177(): pass

    label('loc_177')

    ExecExpressionWithValue(
        0x0009,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x19A
@scena.Code('func_01_19A')
def func_01_19A():
    PlaySE(451, 0x01, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 3, 0x2233)),
            Expr.Return,
        ),
        'loc_1AF',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0001, 0x0004)

    def _loc_1AF(): pass

    label('loc_1AF')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x460),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1BF',
    )

    Call(0, 0x0002)

    def _loc_1BF(): pass

    label('loc_1BF')

    ExecExpressionWithValue(
        0x0008,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x1D1
@scena.Code('func_02_1D1')
def func_02_1D1():
    LoadChip('ED6_DT27/CH03530._CH', 'ED6_DT27/CH03530P._CP', 0)
    LoadChip('ED6_DT29/CH12160._CH', 'ED6_DT29/CH12160P._CP', 1)
    LoadChip('ED6_DT29/CH12161._CH', 'ED6_DT29/CH12161P._CP', 2)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 3)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 4)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_234'),
        (0x00000005, 'loc_241'),
        (0x00000003, 'loc_24E'),
        (0x00000004, 'loc_25B'),
        (0x00000006, 'loc_268'),
        (0x00000007, 'loc_275'),
        (0x00000008, 'loc_282'),
        (0x0000000A, 'loc_28F'),
        (0x0000000E, 'loc_29C'),
        (0x0000000F, 'loc_2A9'),
        (-1, 'loc_2B6'),
    )

    def _loc_234(): pass

    label('loc_234')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 5)

    Jump('loc_2B6')

    def _loc_241(): pass

    label('loc_241')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 5)

    Jump('loc_2B6')

    def _loc_24E(): pass

    label('loc_24E')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 5)

    Jump('loc_2B6')

    def _loc_25B(): pass

    label('loc_25B')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 5)

    Jump('loc_2B6')

    def _loc_268(): pass

    label('loc_268')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 5)

    Jump('loc_2B6')

    def _loc_275(): pass

    label('loc_275')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 5)

    Jump('loc_2B6')

    def _loc_282(): pass

    label('loc_282')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 5)

    Jump('loc_2B6')

    def _loc_28F(): pass

    label('loc_28F')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 5)

    Jump('loc_2B6')

    def _loc_29C(): pass

    label('loc_29C')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 5)

    Jump('loc_2B6')

    def _loc_2A9(): pass

    label('loc_2A9')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 5)

    Jump('loc_2B6')

    def _loc_2B6(): pass

    label('loc_2B6')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000002, 'loc_2E7'),
        (0x00000005, 'loc_2F4'),
        (0x00000003, 'loc_301'),
        (0x00000004, 'loc_30E'),
        (0x00000006, 'loc_31B'),
        (0x00000007, 'loc_328'),
        (0x00000008, 'loc_335'),
        (0x0000000A, 'loc_342'),
        (0x0000000E, 'loc_34F'),
        (0x0000000F, 'loc_35C'),
        (-1, 'loc_369'),
    )

    def _loc_2E7(): pass

    label('loc_2E7')

    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 6)

    Jump('loc_369')

    def _loc_2F4(): pass

    label('loc_2F4')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 6)

    Jump('loc_369')

    def _loc_301(): pass

    label('loc_301')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 6)

    Jump('loc_369')

    def _loc_30E(): pass

    label('loc_30E')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 6)

    Jump('loc_369')

    def _loc_31B(): pass

    label('loc_31B')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 6)

    Jump('loc_369')

    def _loc_328(): pass

    label('loc_328')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 6)

    Jump('loc_369')

    def _loc_335(): pass

    label('loc_335')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 6)

    Jump('loc_369')

    def _loc_342(): pass

    label('loc_342')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 6)

    Jump('loc_369')

    def _loc_34F(): pass

    label('loc_34F')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 6)

    Jump('loc_369')

    def _loc_35C(): pass

    label('loc_35C')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 6)

    Jump('loc_369')

    def _loc_369(): pass

    label('loc_369')

    LoadChip('ED6_DT27/CH04535._CH', 'ED6_DT27/CH04535P._CP', 7)
    LoadChip('ED6_DT27/CH04538._CH', 'ED6_DT27/CH04538P._CP', 8)
    LoadChip('ED6_DT26/CH20503._CH', 'ED6_DT26/CH20503P._CP', 9)
    LoadChip('ED6_DT26/CH20273._CH', 'ED6_DT26/CH20273P._CP', 10)
    LoadEffect(0x00, 'map\\\\mp046_00.eff')

    Return()

# id: 0x0003 offset: 0x3A6
@scena.Code('func_03_3A6')
def func_03_3A6():
    Call(0, 0x0004)
    Call(0, 0x0005)

    Return()

# id: 0x0004 offset: 0x3AF
@scena.Code('func_04_3AF')
def func_04_3AF():
    EventBegin(0x00)
    FadeOut(0, 0, -1)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D0',
    )

    Call(0, 0x0013)
    Call(0, 0x0014)

    def _loc_3D0(): pass

    label('loc_3D0')

    Call(0, 0x0002)
    CameraMove(-720, 0, -17580, 0)
    OP_67(0, 5710, -10000, 0)
    CameraSetDistance(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    CreateThread(0x0101, 0x00, 0x00, func_09_35B2)
    Sleep(80)

    CreateThread(0x0102, 0x00, 0x00, func_0A_35D8)
    Sleep(50)

    CreateThread(0x00F8, 0x00, 0x00, func_0B_35FE)
    Sleep(100)

    CreateThread(0x00F9, 0x00, 0x00, func_0C_3624)

    @scena.Lambda('lambda_0442')
    def lambda_0442():
        CameraSetDistance(3960, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0442)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410001V#1020F#6P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410002V#1042F#6P出来了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_04B4')
    def lambda_04B4():
        CameraMove(-1010, 0, 4630, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_04B4)

    CreateThread(0x0101, 0x01, 0x00, func_0D_364A)
    Sleep(200)

    CreateThread(0x0102, 0x01, 0x00, func_0E_3679)
    Sleep(100)

    CreateThread(0x00F8, 0x01, 0x00, func_0F_368E)
    Sleep(100)

    CreateThread(0x00F9, 0x01, 0x00, func_10_36A3)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010410003V#1002F#5P好像已经登上\n',
            '相当的高度了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrSetDirection(0x0101, 0, 400)

    ChrTalk(
        0x0101,
        (
            '#0010410004V#1004F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_057A')
    def lambda_057A():
        CameraMove(-1540, 0, 34870, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_057A)

    @scena.Lambda('lambda_0592')
    def lambda_0592():
        OP_67(0, 4200, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0592)

    @scena.Lambda('lambda_05AA')
    def lambda_05AA():
        CameraSetDistance(2780, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_05AA)

    @scena.Lambda('lambda_05BA')
    def lambda_05BA():
        OP_6E(382, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_05BA)

    @scena.Lambda('lambda_05CA')
    def lambda_05CA():
        OP_6C(327000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_05CA)

    WaitForThreadExit(0x0101, 0x0002)
    Sleep(1000)

    @scena.Lambda('lambda_05E4')
    def lambda_05E4():
        ChrWalkTo(0x00FE, 1710, 0, 25450, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05E4)

    Sleep(50)

    @scena.Lambda('lambda_0604')
    def lambda_0604():
        ChrWalkTo(0x00FE, 350, 0, 25450, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0604)

    Sleep(100)

    @scena.Lambda('lambda_0624')
    def lambda_0624():
        ChrWalkTo(0x00FE, 1990, 0, 24000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0624)

    Sleep(60)

    @scena.Lambda('lambda_0644')
    def lambda_0644():
        ChrWalkTo(0x00FE, 620, 0, 24000, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_0644)

    @scena.Lambda('lambda_065F')
    def lambda_065F():
        OP_6C(315000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_065F)

    @scena.Lambda('lambda_066F')
    def lambda_066F():
        CameraMove(-1140, 0, 29790, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_066F)

    @scena.Lambda('lambda_0687')
    def lambda_0687():
        OP_67(0, 4780, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0687)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010410005V#1015F#6P那个……是什么呢？',
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
        'loc_73B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410006V#072F#6P……唔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410007V像是什么东西的终端\n',
            '不过感觉好奇怪啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACF')

    def _loc_73B(): pass

    label('loc_73B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7B5',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410008V#555F#6P哼……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050410009V像是什么东西的终端……\n',
            '不过摆在这种地方，不觉得太奇怪了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACF')

    def _loc_7B5(): pass

    label('loc_7B5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_835',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410010V<FIXME>#178F#5Pふむ……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410011V何かの端末のようだが\n',
            '妙に思わせぶりに\n',
            '置かれているな……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACF')

    def _loc_835(): pass

    label('loc_835')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8AA',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410012V#033F#6P哟……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040410013V#035F像是什么装置的终端，\n',
            '不过放在这里明显像是陷阱啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACF')

    def _loc_8AA(): pass

    label('loc_8AA')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_913',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410014V#1063F#6P唔～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180410015V像是什么终端设备，\n',
            '不过放在这里太可疑了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACF')

    def _loc_913(): pass

    label('loc_913')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_97D',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410016V#023F#6P哎呀……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410017V像是什么设备的终端，\n',
            '不过感觉太不对劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACF')

    def _loc_97D(): pass

    label('loc_97D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9EB',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410018V#212F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090410019V像是什么东西的终端，\n',
            '不过在这里出现也太奇怪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACF')

    def _loc_9EB(): pass

    label('loc_9EB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A53',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410020V#270F#6P嗯……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110410021V像是什么东西的终端，\n',
            '感觉像是什么陷阱呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_ACF')

    def _loc_A53(): pass

    label('loc_A53')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_ACF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410022V#1164F#6P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060410023V#1162F像是什么装置的终端，\n',
            '不过总觉得很可疑啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_ACF(): pass

    label('loc_ACF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_B6F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410024V#062F#6P那，看来要\n',
            '好好调查一下为好呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410025V#1035F#5P不……\n',
            '还是等一下再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070410026V#064F#6P啊……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105C')

    def _loc_B6F(): pass

    label('loc_B6F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_C0D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410027V#1162F#6P看来有必要\n',
            '调查一下看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410025V#1035F#5P不……\n',
            '还是等一下再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060410029V#1164F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105C')

    def _loc_C0D(): pass

    label('loc_C0D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CA7',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410030V#272F#6P看来最好是\n',
            '好好调查一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410031V#1035F#5P不……\n',
            '还是等一下再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0110410032V#270F#6P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105C')

    def _loc_CA7(): pass

    label('loc_CA7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_D43',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410033V#212F#6P看来最好是\n',
            '好好调查一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410025V#1035F#5P不……\n',
            '还是等一下再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010B,
        (
            '#0090410035V#213F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105C')

    def _loc_D43(): pass

    label('loc_D43')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_DE1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410036V#022F#6P这似乎要好好\n',
            '调查一下比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410037V#1035F#5P不……\n',
            '还是等一下再说吧。',
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

    Jump('loc_105C')

    def _loc_DE1(): pass

    label('loc_DE1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E81',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410039V#1063F#6P这似乎要好好\n',
            '调查一下比较好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410037V#1035F#5P不……\n',
            '还是等一下再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0109,
        (
            '#0180410041V#1064F#6P哦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105C')

    def _loc_E81(): pass

    label('loc_E81')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F21',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410042V#035F#6P呼，这看来需要\n',
            '好好调查一下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410037V#1035F#5P不……\n',
            '还是等一下再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410044V#033F#6P哎呀……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105C')

    def _loc_F21(): pass

    label('loc_F21')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FBD',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410045V#178F#6P看来有必要\n',
            '调查一下看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410031V#1035F#5P不……\n',
            '还是等一下再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010F,
        (
            '#0100410047V#173F#6P咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_105C')

    def _loc_FBD(): pass

    label('loc_FBD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_105C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410048V#051F#6P嘿，这可有必要\n',
            '好好地调查一下啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410037V#1035F#5P不……\n',
            '还是等一下再说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050410050V#052F#6P什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_105C(): pass

    label('loc_105C')

    ChrSetChipByIndex(0x0008, 7)
    ChrSetPos(0x0008, 3070, 6620, 33000, 180)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0008, 0x0080)
    OP_20(0x000003E8)
    OP_21()

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0170410051V#6P呼呼，不愧是『漆黑之牙』。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410052V不仅善于隐藏自己的气息，\n',
            '也很擅长察觉别人的藏匿啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1146',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1184')

    def _loc_1146(): pass

    label('loc_1146')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_116D',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1184')

    def _loc_116D(): pass

    label('loc_116D')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_1184(): pass

    label('loc_1184')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11B0',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_11EE')

    def _loc_11B0(): pass

    label('loc_11B0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11D7',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_11EE')

    def _loc_11D7(): pass

    label('loc_11D7')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_11EE(): pass

    label('loc_11EE')

    Sleep(500)

    PlayBGM(111)
    Sleep(500)

    Fade(1000)
    OP_71(0x0000, 0x0004)
    MapClearFlags(0x00000010)
    CameraMove(3030, 4570, 31690, 0)
    OP_67(0, 3680, -10000, 0)
    CameraSetDistance(2670, 0)
    OP_6C(0, 0)
    OP_6E(382, 0)

    @scena.Lambda('lambda_124C')
    def lambda_124C():
        CameraMove(3030, 7260, 31690, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_124C)

    @scena.Lambda('lambda_1264')
    def lambda_1264():
        OP_67(0, 3400, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1264)

    Sleep(1500)

    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(266, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_12C0')
    def lambda_12C0():
        CameraSetDistance(2390, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_12C0)

    Sleep(1000)

    StopEffect(0x00, 0x02)
    CreateThread(0x0008, 0x03, 0x00, func_06_347E)
    Sleep(500)

    @scena.Lambda('lambda_12E4')
    def lambda_12E4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_12E4)

    WaitForThreadExit(0x0008, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010410053V#1020F#2P假、假面男……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_136D',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410054V#270F FIXME （………何だ、この男……？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_136D(): pass

    label('loc_136D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_13FF',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410055V#178F FIXME （……翡翠の塔に現れた男か……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410056V#176F（殿下の前に、何度も\n',
            '  現れているという話だが……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13FF(): pass

    label('loc_13FF')

    ChrTalk(
        0x0102,
        (
            '#0020410057V#1042F#5P布卢布兰……是你吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_154D',
    )

    ChrTalk(
        0x0008,
        (
            '#0170410058V#231F#5P欢迎，约修亚……\n',
            '还有艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410059V虽然我的公主和好对手没来，\n',
            '令我无比遗憾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410060V但还是让我衷心向各位表示欢迎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410061V#1002F#2P欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410062V#1042F#5P……看来你就是\n',
            '第一道障碍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B0E')

    def _loc_154D(): pass

    label('loc_154D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1765',
    )

    ChrTalk(
        0x0008,
        (
            '#0170410063V#231F#5P约修亚、艾丝蒂尔·布莱特，\n',
            '还有我高贵的公主也来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410064V虽然我的好对手不在\n',
            '让人略感遗憾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410060V但还是让我衷心向各位表示欢迎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1680',
    )

    ChrTalk(
        0x0101,
        (
            '#0010410061V#1002F#2P欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060410067V#1162F#5P……看来你就是\n',
            '第一道障碍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1762')

    def _loc_1680(): pass

    label('loc_1680')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1762',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410068V#176F歓迎、か……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410069V#172F……降りて来い。\n',
            '私がこの場で成敗してやろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060410070V#1165F FIXME （ユリアさん、本気ですね……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060410071V#1162F#5P……看来你就是\n',
            '第一道障碍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1762(): pass

    label('loc_1762')

    Jump('loc_1B0E')

    def _loc_1765(): pass

    label('loc_1765')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19C5',
    )

    ChrTalk(
        0x0008,
        (
            '#0170410072V#231F#5P约修亚、艾丝蒂尔·布莱特，\n',
            '还有我的好对手也来了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410073V高贵的公主不在\n',
            '让人略感遗憾……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410060V但还是让我衷心向各位表示欢迎吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1891',
    )

    ChrTalk(
        0x0101,
        (
            '#0010410061V#1002F#2P欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410076V#035F#5P呼，看来你就是\n',
            '第一道障碍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19C2')

    def _loc_1891(): pass

    label('loc_1891')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_19C2',
    )

    ChrTalk(
        0x0110,
        (
            '#0111880001V#276F FIXME ……成る程な。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110410077V#272Fこのお調子者の\n',
            '同類というわけか。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410078V#34F FIXME 同類だなんて……\n',
            'ミュラー君ひどいッ！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0110,
        (
            '#0110410079V#272Fフン、外れてはいないだろう。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110410080V#270F……しかしどうやら、あの男が\n',
            '最初の障害ということらしいな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19C2(): pass

    label('loc_19C2')

    Jump('loc_1B0E')

    def _loc_19C5(): pass

    label('loc_19C5')

    ChrTalk(
        0x0008,
        (
            '#0170410058V#231F#5P欢迎，约修亚……\n',
            '还有艾丝蒂尔·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410082V而且没想到，连我的公主\n',
            '和好对手也在一起……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410083V请让我怪盗绅士，以最高的喜悦\n',
            '欢迎诸位的到来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410084V#1002F#2P欢、欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410085V#035F#5P呼，相当做作的\n',
            '登场方式嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060410067V#1162F#5P……看来你就是\n',
            '第一道障碍了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B0E(): pass

    label('loc_1B0E')

    ChrTalk(
        0x0008,
        (
            '#0170410087V#230F#5P呵呵……\n',
            '是第一道，也是最后一道障碍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410088V摆在这里的装置是\n',
            '锁住通往『中枢塔』上层之门\n',
            '的终端。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410089V只要这个装置还在运转，\n',
            '诸位就永远无法到达『环』的所在处。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410090V#1019F#2P你、你说什么～！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410091V#1035F#5P……布卢布兰。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410092V#1042F在为了此次计划\n',
            '而来到利贝尔的众位执行者中，\n',
            '你和我们的因缘应该是最浅的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410093V既然如此，你听命于教授，\n',
            '来与我们作战的理由到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170410094V#230F#5P呵呵……我其实\n',
            '并不是听命于教授。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410095V如你所知，我们『执行者』没有义务遵从\n',
            '违背自己意愿的命令。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410096V不要说是『使徒』，\n',
            '纵使是『盟主』的命令也一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410097V#231F呵呵，不过身为教授人偶的你\n',
            '似乎是有些不同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410098V#1043F#5P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410099V#1003F#2P约修亚……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170410100V#232F#5P我之所以拘泥于此，理由只有一个…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410101V那就是这里有值得我盗取的\n',
            '美妙之物。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410102V为了它，我才会守在此地。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2141',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F2C',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410103V#178F#5P值得盗取的美妙之物……\n',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410104V你到底在说什么！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213E')

    def _loc_1F2C(): pass

    label('loc_1F2C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F7E',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410105V#555F#5P值得盗取的美妙之物……\n',
            '那究竟是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213E')

    def _loc_1F7E(): pass

    label('loc_1F7E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FD4',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410106V#022F#5P值得盗取的美妙之物……\n',
            '那到底是什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213E')

    def _loc_1FD4(): pass

    label('loc_1FD4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2028',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410107V#065F#5P值得盗取的美妙之物……\n',
            '那、那到底是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213E')

    def _loc_2028(): pass

    label('loc_2028')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_207A',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410108V#214F#5P值得盗取的美妙之物……\n',
            '那到底是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213E')

    def _loc_207A(): pass

    label('loc_207A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20CD',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410109V#1063F#5P值得盗取的美妙之物……\n',
            '那究竟是什么呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213E')

    def _loc_20CD(): pass

    label('loc_20CD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_213E',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410110V#270F#5P盗む価値のある美しい物……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110410111V#272F何を訳の分からんことを……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_213E(): pass

    label('loc_213E')

    Jump('loc_225F')

    def _loc_2141(): pass

    label('loc_2141')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_21A3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410112V#1163F#5P值得盗取的美妙之物……\n',
            '那到底是什么东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_225F')

    def _loc_21A3(): pass

    label('loc_21A3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2202',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410113V#033F#5P值得盗取的美妙之物……\n',
            '唔，那到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_225F')

    def _loc_2202(): pass

    label('loc_2202')

    ChrTalk(
        0x0105,
        (
            '#0060410114V#1163F#5P值得盗取的美妙之物……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410115V#033F#5P唔，那到底是什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_225F(): pass

    label('loc_225F')

    ChrTalk(
        0x0008,
        (
            '#0170410116V#231F#5P呵呵……\n',
            '那就是诸位的『希望』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410117V#1020F#2P#3S！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0170410118V#231F#5P正因面临着逆境，\n',
            '所谓的『希望』才会散发出美丽的光芒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410119V为了看到那璀灿绚烂的光辉，\n',
            '我才会在此等待诸位。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410120V#232F即使这『希望』的光芒如夏日的烟火\n',
            '一般转瞬即逝……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410121V#234F我也希望见证它的存在！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0800)
    ChrSetChipByIndex(0x0008, 8)
    ChrSetSubChip(0x0008, 0)
    OP_99(0x0008, 0x00, 0x0E, 2000)
    Sleep(200)

    Fade(1000)
    OP_72(0x0000, 0x0004)
    CameraMove(2800, 4330, 23050, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3920, 0)
    OP_6C(315000, 0)
    OP_6E(340, 0)
    OP_0D()

    @scena.Lambda('lambda_241E')
    def lambda_241E():
        OP_67(0, 4680, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_241E)

    CreateThread(0x0009, 0x00, 0x00, func_07_34C6)
    Sleep(500)

    CreateThread(0x000A, 0x00, 0x00, func_08_353C)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24A2',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_24E0')

    def _loc_24A2(): pass

    label('loc_24A2')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_24C9',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_24E0')

    def _loc_24C9(): pass

    label('loc_24C9')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_24E0(): pass

    label('loc_24E0')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_250C',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_254A')

    def _loc_250C(): pass

    label('loc_250C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2533',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_254A')

    def _loc_2533(): pass

    label('loc_2533')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_254A(): pass

    label('loc_254A')

    Sleep(1000)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 4)
    ChrSetChipByIndex(0x00F8, 5)
    ChrSetChipByIndex(0x00F9, 6)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)

    @scena.Lambda('lambda_2587')
    def lambda_2587():
        ChrSetDirection(0x00FE, 225, 400)

        ExitThread()

    DispatchAsync(0x00F9, 0x0001, lambda_2587)

    Sleep(100)

    ChrSetDirection(0x00F8, 135, 400)
    OP_0D()
    Sleep(300)

    Fade(250)
    ChrClearFlags(0x0008, 0x0800)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 7)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170340819V#231F来吧，就让我看看！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410123V名为希望的宝石\n',
            '在破碎散落时所绽放出的光辉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_26E1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010410124V#1005F#6P别，别在那里\n',
            '说些自以为是的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060410125V#1167F#5P那我们也向你证明吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060410126V#1162F由羁绊所产生出的希望\n',
            '是绝不会破碎散落的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AF')

    def _loc_26E1(): pass

    label('loc_26E1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27AB',
    )

    ChrTalk(
        0x0101,
        (
            '#0010410124V#1005F#6P少，少在那里\n',
            '说些自以为是的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410128V#035F#5P呼，那就让你好好领会一下吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040410129V#530F只要有爱，希望的灯火\n',
            '就会永远燃烧下去的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AF')

    def _loc_27AB(): pass

    label('loc_27AB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_28AF',
    )

    ChrTalk(
        0x0101,
        (
            '#0010410124V#1005F#6P少，少在那里\n',
            '说些自以为是的话！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060410125V#1167F#5P那我们也向你证明吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060410126V#1162F由羁绊所产生出的希望\n',
            '是绝不会破碎散落的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410133V#035F#5P只要有爱，希望的灯火\n',
            '就会永远燃烧下去的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28AF(): pass

    label('loc_28AF')

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)

    @scena.Lambda('lambda_28C3')
    def lambda_28C3():
        CameraMove(190, 980, 24880, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_28C3)

    @scena.Lambda('lambda_28DB')
    def lambda_28DB():
        OP_67(0, 4830, -10000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_28DB)

    @scena.Lambda('lambda_28F3')
    def lambda_28F3():
        CameraSetDistance(2800, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_28F3)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 10)
    PlaySE(163, 0x00, 0x64)

    @scena.Lambda('lambda_2912')
    def lambda_2912():
        ChrJumpTo(0x00FE, 900, 0, 25670, 800, 14000)

        ExitThread()

    DispatchAsync(0x0008, 0x0000, lambda_2912)

    @scena.Lambda('lambda_2930')
    def lambda_2930():
        ChrWalkTo(0x00FE, -420, 800, 23500, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_2930)

    Sleep(80)

    @scena.Lambda('lambda_2950')
    def lambda_2950():
        ChrWalkTo(0x00FE, 2380, 800, 23170, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_2950)

    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0008, 0x00)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000460, 0x00000000, 0x00, 0x0000, 0xFF)

    Return()

# id: 0x0005 offset: 0x2988
@scena.Code('func_05_2988')
def func_05_2988():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x0008, 0x00)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    EventBegin(0x00)
    ChrSetPos(0x0101, 1370, 0, 20520, 0)
    ChrSetPos(0x0102, -70, 0, 20470, 0)
    ChrSetPos(0x00F8, 1600, 0, 18950, 0)
    ChrSetPos(0x00F9, -70, 0, 19040, 0)
    ChrSetPos(0x0008, 300, 0, 28070, 180)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 9)
    CameraMove(-410, 0, 24050, 0)
    OP_67(0, 5460, -10000, 0)
    CameraSetDistance(4200, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    CameraSetDistance(4000, 2000)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0170410134V#236F#2P……唔……不可能………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410135V居然将我的假面……\n',
            '……打出裂痕……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410136V#1005F#6P呼……呼……\n',
            '怎样……体会到了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410137V#1035F#6P……破碎散落的\n',
            '看来是你的傲慢呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2BA8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410138V#1162F羁绊所产生出的希望有多强大……\n',
            '你现在明白了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CCE')

    def _loc_2BA8(): pass

    label('loc_2BA8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C15',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410139V#030F呼……\n',
            '让希望之灯火燃烧不断\n',
            '的爱的伟大，你已经体会到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2CCE')

    def _loc_2C15(): pass

    label('loc_2C15')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CCE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410138V#1162F羁绊所产生出的希望有多强大……\n',
            '你现在明白了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040410141V#030F呼……\n',
            '而让希望之灯火燃烧不断\n',
            '的“爱”的伟大，你也已经体会到了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2CCE(): pass

    label('loc_2CCE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D31',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410142V#178F FIXME ……これに懲りたならば、\n',
            '二度と殿下の前に現れぬことだ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D31(): pass

    label('loc_2D31')

    ChrTalk(
        0x0008,
        (
            '#0170410143V#236F#2P……………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410144V#237F好吧……\n',
            '按照约定，我就撤退好了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410145V但是，教授的游戏\n',
            '才刚刚开始而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410146V你们最好有所觉悟，\n',
            '如这次一般的幸运未必还会有第二次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    ChrSetSubChip(0x0008, 8)
    OP_0D()
    Sleep(100)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x10),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(200)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(100)

    @scena.Lambda('lambda_2E4A')
    def lambda_2E4A():
        CameraMove(-410, 0, 25050, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_2E4A)

    @scena.Lambda('lambda_2E62')
    def lambda_2E62():
        OP_67(0, 4800, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E62)

    PlayEffect(0x00, 0x00, 0x0008, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(266, 0x00, 0x64)
    Sleep(3000)

    ChrTalk(
        0x0008,
        (
            '#0170410147V#238F#2P别忘了……\n',
            '诸位可是将我击退的人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410148V越过矗立在面前的绝望之壁后，\n',
            '最终一定能到达美丽的彼岸吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170410149V……那么，再见吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 2000)
    StopEffect(0x00, 0x02)
    CreateThread(0x0008, 0x03, 0x00, func_06_347E)
    Sleep(1500)

    ChrSetFlags(0x0008, 0x0080)
    WaitForThreadExit(0x0101, 0x0000)

    ChrTalk(
        0x0101,
        (
            '#0010410150V#1026F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x0102,
        (
            '#0020410151V#1035F#5P……看来……\n',
            '真的已经离开了啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410152V#1040F他的自尊心很强，\n',
            '我想应该不会违背约定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410153V#1025F#6P是嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3086',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410154V#031F#6P哼哼……\n',
            '虽是敌人，但还是值得赞赏吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3086(): pass

    label('loc_3086')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_30BF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410155V#1168F#6P……这就放心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_30BF(): pass

    label('loc_30BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3107',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410156V#210F#6P呼……\n',
            '真是个只会添乱的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322E')

    def _loc_3107(): pass

    label('loc_3107')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_314F',
    )

    ChrTalk(
        0x0103,
        (
            '#0030410157V#524F#6P呼……\n',
            '真是个只会添乱的男人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322E')

    def _loc_314F(): pass

    label('loc_314F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3199',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410158V#051F#6P嘿……\n',
            '真是个只会添麻烦的小子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322E')

    def _loc_3199(): pass

    label('loc_3199')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_31E3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410159V#071F#6P哈哈……\n',
            '真是个只会添乱的人啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_322E')

    def _loc_31E3(): pass

    label('loc_31E3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_322E',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410160V#272F FIXME フン……\n',
            '人騒がせな男だったな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_322E(): pass

    label('loc_322E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_326F',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410161V#1068F#6P呀～……\n',
            '还好撤退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_32AC')

    def _loc_326F(): pass

    label('loc_326F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_32AC',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410162V#067F#6P嘿嘿……\n',
            '还好撤退了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32AC(): pass

    label('loc_32AC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3325',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410163V#176F FIXME ふう…………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410164V（……これでようやく\n',
            '  不安要素の１つは消えたか。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3325(): pass

    label('loc_3325')

    @scena.Lambda('lambda_332B')
    def lambda_332B():
        CameraMove(340, 0, 21000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_332B)

    @scena.Lambda('lambda_3343')
    def lambda_3343():
        OP_67(0, 6500, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3343)

    @scena.Lambda('lambda_335B')
    def lambda_335B():
        CameraSetDistance(3760, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_335B)

    WaitForThreadExit(0x0101, 0x0000)
    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    OP_0D()
    Sleep(500)

    ChrTurnDirection(0x0102, 0x0101, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020410165V#1040F#5P那么\n',
            '就把那里的终端停止吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410166V这样应该能打开\n',
            '通往上层的门了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010410167V#1006F#4P嗯……明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3450',
    )

    SetScenaFlags(ScenaFlag(0x0447, 7, 0x223F))

    def _loc_3450(): pass

    label('loc_3450')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3461',
    )

    SetScenaFlags(ScenaFlag(0x0448, 1, 0x2241))

    def _loc_3461(): pass

    label('loc_3461')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3472',
    )

    SetScenaFlags(ScenaFlag(0x045B, 0, 0x22D8))

    def _loc_3472(): pass

    label('loc_3472')

    SetScenaFlags(ScenaFlag(0x0446, 2, 0x2232))
    OP_28(0x009F, 0x01, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0006 offset: 0x347E
@scena.Code('func_06_347E')
def func_06_347E():
    Sleep(300)

    OP_24(0x010A, 0x5A)
    Sleep(300)

    OP_24(0x010A, 0x50)
    Sleep(300)

    OP_24(0x010A, 0x46)
    Sleep(300)

    OP_24(0x010A, 0x3C)
    Sleep(300)

    OP_24(0x010A, 0x32)
    Sleep(300)

    OP_24(0x010A, 0x28)
    Sleep(300)

    OP_24(0x010A, 0x1E)
    Sleep(300)

    OP_23(0x010A)

    Return()

# id: 0x0007 offset: 0x34C6
@scena.Code('func_07_34C6')
def func_07_34C6():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetChipByIndex(0x00FE, 1)
    ChrSetPos(0x00FE, -2900, 15000, 20260, 45)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_34EC')
    def lambda_34EC():
        ChrJumpTo(0x00FE, -2900, 800, 20260, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_34EC)

    WaitForThreadExit(0x00FE, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    OP_99(0x00FE, 0x00, 0x07, 1500)

    @scena.Lambda('lambda_352E')
    def lambda_352E():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_352E')

    DispatchAsync2(0x00FE, 0x0003, lambda_352E)

    Return()

# id: 0x0008 offset: 0x353C
@scena.Code('func_08_353C')
def func_08_353C():
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetChipByIndex(0x00FE, 1)
    ChrSetPos(0x00FE, 5630, 15000, 19970, 315)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_3562')
    def lambda_3562():
        ChrJumpTo(0x00FE, 5630, 800, 19970, 1000, 5000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_3562)

    WaitForThreadExit(0x00FE, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)
    OP_99(0x00FE, 0x00, 0x07, 1500)

    @scena.Lambda('lambda_35A4')
    def lambda_35A4():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_35A4')

    DispatchAsync2(0x00FE, 0x0003, lambda_35A4)

    Return()

# id: 0x0009 offset: 0x35B2
@scena.Code('func_09_35B2')
def func_09_35B2():
    ChrSetPos(0x00FE, 870, 0, -25040, 0)
    ChrWalkTo(0x00FE, 870, 0, -18040, 3000, 0x00)

    Return()

# id: 0x000A offset: 0x35D8
@scena.Code('func_0A_35D8')
def func_0A_35D8():
    ChrSetPos(0x00FE, -390, 0, -25050, 0)
    ChrWalkTo(0x00FE, -390, 0, -18050, 3000, 0x00)

    Return()

# id: 0x000B offset: 0x35FE
@scena.Code('func_0B_35FE')
def func_0B_35FE():
    ChrSetPos(0x00FE, 1150, 0, -26400, 0)
    ChrWalkTo(0x00FE, 1150, 0, -19400, 3000, 0x00)

    Return()

# id: 0x000C offset: 0x3624
@scena.Code('func_0C_3624')
def func_0C_3624():
    ChrSetPos(0x00FE, -210, 0, -26410, 0)
    ChrWalkTo(0x00FE, -210, 0, -19410, 3000, 0x00)

    Return()

# id: 0x000D offset: 0x364A
@scena.Code('func_0D_364A')
def func_0D_364A():
    ChrWalkTo(0x00FE, 570, 0, 4450, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    Sleep(500)

    ChrSetDirection(0x00FE, 0, 400)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x000E offset: 0x3679
@scena.Code('func_0E_3679')
def func_0E_3679():
    ChrWalkTo(0x00FE, -660, 0, 4200, 4000, 0x00)

    Return()

# id: 0x000F offset: 0x368E
@scena.Code('func_0F_368E')
def func_0F_368E():
    ChrWalkTo(0x00FE, 960, 0, 3010, 4000, 0x00)

    Return()

# id: 0x0010 offset: 0x36A3
@scena.Code('func_10_36A3')
def func_10_36A3():
    ChrWalkTo(0x00FE, -410, 0, 2950, 4000, 0x00)

    Return()

# id: 0x0011 offset: 0x36B8
@scena.Code('func_11_36B8')
def func_11_36B8():
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '解除通向上层区域的隔离壁，\n',
            '以及传送门的锁定。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(200)

    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/C5301._SN', 114, 0, 0)
    IdleLoop()

    Return()

# id: 0x0012 offset: 0x3722
@scena.Code('func_12_3722')
def func_12_3722():
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
        'loc_3739',
    )

    Call(0, 0x0013)
    Call(0, 0x0014)

    def _loc_3739(): pass

    label('loc_3739')

    CameraMove(-390, 0, 32400, 0)
    OP_67(0, 6020, -10000, 0)
    CameraSetDistance(3540, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 920, 0, 31200, 0)
    ChrSetPos(0x0102, -200, 0, 31200, 0)
    ChrSetPos(0x00F8, 1490, 0, 29660, 0)
    ChrSetPos(0x00F9, -40, 0, 29880, 0)
    FadeIn(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '通向上层区域的隔离墙，\n',
            '以及传送门的锁定已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_71(0x0001, 0x0004)
    OP_0D()
    Sleep(500)

    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x0446, 3, 0x2233))
    OP_28(0x009F, 0x01, 0x0008)
    EventEnd(0x00)

    Return()

# id: 0x0013 offset: 0x3837
@scena.Code('func_13_3837')
def func_13_3837():
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
        (0x00000000, 'loc_38B1'),
        (0x00000001, 'loc_38B7'),
        (-1, 'loc_38BD'),
    )

    def _loc_38B1(): pass

    label('loc_38B1')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_38BD')

    def _loc_38B7(): pass

    label('loc_38B7')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_38BD')

    def _loc_38BD(): pass

    label('loc_38BD')

    Return()

# id: 0x0014 offset: 0x38BE
@scena.Code('func_14_38BE')
def func_14_38BE():
    FadeOut(0, 0, -1)
    CameraMove(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)

    FadeIn(0, 0)
    OP_0D()

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['约修亚'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['雪拉扎德'],
            ChrTable['科洛丝'],
            ChrTable['奥利维尔'],
            ChrTable['提妲'],
            ChrTable['金'],
            ChrTable['凯文神父'],
            ChrTable['乔丝特'],
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
