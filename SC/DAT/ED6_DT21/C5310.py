import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5310_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5310   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Other'
    header.mapModel       = 'C5310.x'
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
            dword_10            = 0,
            chipIndex           = 0,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E1,
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
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01E1,
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
        ScenaNpcData(
            name                = '雪拉扎德',
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

# id: 0x10002 offset: 0x188
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x188
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x188
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
            talkFunctionIndex   = 0x0016,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1AC
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_1BD',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_17_5584)

    Jump('loc_20A')

    def _loc_1BD(): pass

    label('loc_1BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 7, 0x2237)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            Expr.Ez,
            Expr.Nez64,
            (Expr.PushValueByIndex, 0x0),
            (Expr.PushLong, 0x64),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20A',
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
        'loc_1E7',
    )

    Event(0, func_18_569B)

    Jump('loc_20A')

    def _loc_1E7(): pass

    label('loc_1E7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_201',
    )

    MapSetFlags(0x10000000)
    Event(0, func_04_790)

    Jump('loc_20A')

    def _loc_201(): pass

    label('loc_201')

    MapSetFlags(0x10000000)
    Event(0, func_0F_22A9)

    def _loc_20A(): pass

    label('loc_20A')

    Return()

# id: 0x0001 offset: 0x20B
@scena.Code('func_01_20B')
def func_01_20B():
    PlaySE(451, 0x01, 0x64)
    OP_71(0x0001, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 1, 0x2239)),
            Expr.Return,
        ),
        'loc_225',
    )

    OP_64(0x00, 0x0001)
    OP_71(0x0002, 0x0004)

    def _loc_225(): pass

    label('loc_225')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0446, 7, 0x2237)),
            (Expr.TestScenaFlags, ScenaFlag(0x0447, 0, 0x2238)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_235',
    )

    OP_72(0x0004, 0x0004)

    def _loc_235(): pass

    label('loc_235')

    If(
        (
            (Expr.PushValueByIndex, 0x29),
            (Expr.PushLong, 0x462),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_263',
    )

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_256',
    )

    Call(0, 0x0002)

    Jump('loc_263')

    def _loc_256(): pass

    label('loc_256')

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Call(0, 0x0003)

    def _loc_263(): pass

    label('loc_263')

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

# id: 0x0002 offset: 0x286
@scena.Code('func_02_286')
def func_02_286():
    LoadChip('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP', 0)
    LoadChip('ED6_DT29/CH12380._CH', 'ED6_DT29/CH12380P._CP', 1)
    LoadChip('ED6_DT09/CH10910._CH', 'ED6_DT09/CH10910P._CP', 2)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 3)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 4)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 5)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 6)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_2F9'),
        (0x00000003, 'loc_310'),
        (0x00000004, 'loc_327'),
        (0x00000006, 'loc_33E'),
        (0x00000007, 'loc_355'),
        (0x00000008, 'loc_36C'),
        (0x0000000A, 'loc_383'),
        (0x0000000E, 'loc_39A'),
        (0x0000000F, 'loc_3B1'),
        (-1, 'loc_3C8'),
    )

    def _loc_2F9(): pass

    label('loc_2F9')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 7)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 8)

    Jump('loc_3C8')

    def _loc_310(): pass

    label('loc_310')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 7)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 8)

    Jump('loc_3C8')

    def _loc_327(): pass

    label('loc_327')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 7)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 8)

    Jump('loc_3C8')

    def _loc_33E(): pass

    label('loc_33E')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 7)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 8)

    Jump('loc_3C8')

    def _loc_355(): pass

    label('loc_355')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 7)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 8)

    Jump('loc_3C8')

    def _loc_36C(): pass

    label('loc_36C')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 7)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 8)

    Jump('loc_3C8')

    def _loc_383(): pass

    label('loc_383')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 7)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 8)

    Jump('loc_3C8')

    def _loc_39A(): pass

    label('loc_39A')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 7)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 8)

    Jump('loc_3C8')

    def _loc_3B1(): pass

    label('loc_3B1')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 7)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 8)

    Jump('loc_3C8')

    def _loc_3C8(): pass

    label('loc_3C8')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_3F5'),
        (0x00000003, 'loc_40C'),
        (0x00000004, 'loc_423'),
        (0x00000006, 'loc_43A'),
        (0x00000007, 'loc_451'),
        (0x00000008, 'loc_468'),
        (0x0000000A, 'loc_47F'),
        (0x0000000E, 'loc_496'),
        (0x0000000F, 'loc_4AD'),
        (-1, 'loc_4C4'),
    )

    def _loc_3F5(): pass

    label('loc_3F5')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 9)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 10)

    Jump('loc_4C4')

    def _loc_40C(): pass

    label('loc_40C')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 9)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 10)

    Jump('loc_4C4')

    def _loc_423(): pass

    label('loc_423')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 9)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 10)

    Jump('loc_4C4')

    def _loc_43A(): pass

    label('loc_43A')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 9)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 10)

    Jump('loc_4C4')

    def _loc_451(): pass

    label('loc_451')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 9)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 10)

    Jump('loc_4C4')

    def _loc_468(): pass

    label('loc_468')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 9)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 10)

    Jump('loc_4C4')

    def _loc_47F(): pass

    label('loc_47F')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 9)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 10)

    Jump('loc_4C4')

    def _loc_496(): pass

    label('loc_496')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 9)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 10)

    Jump('loc_4C4')

    def _loc_4AD(): pass

    label('loc_4AD')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 9)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 10)

    Jump('loc_4C4')

    def _loc_4C4(): pass

    label('loc_4C4')

    LoadChip('ED6_DT27/CH04524._CH', 'ED6_DT27/CH04524P._CP', 11)
    LoadChip('ED6_DT27/CH04525._CH', 'ED6_DT27/CH04525P._CP', 12)
    LoadChip('ED6_DT27/CH04526._CH', 'ED6_DT27/CH04526P._CP', 13)
    LoadChip('ED6_DT29/CH12381._CH', 'ED6_DT29/CH12381P._CP', 14)
    LoadChip('ED6_DT09/CH10911._CH', 'ED6_DT09/CH10911P._CP', 15)

    Return()

# id: 0x0003 offset: 0x4F7
@scena.Code('func_03_4F7')
def func_03_4F7():
    LoadChip('ED6_DT27/CH03520._CH', 'ED6_DT27/CH03520P._CP', 0)
    LoadChip('ED6_DT29/CH12380._CH', 'ED6_DT29/CH12380P._CP', 1)
    LoadChip('ED6_DT09/CH10910._CH', 'ED6_DT09/CH10910P._CP', 2)
    LoadChip('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP', 3)
    LoadChip('ED6_DT27/CH04001._CH', 'ED6_DT27/CH04001P._CP', 4)
    LoadChip('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP', 5)
    LoadChip('ED6_DT27/CH04011._CH', 'ED6_DT27/CH04011P._CP', 6)
    LoadChip('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP', 7)
    LoadChip('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP', 8)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_57E'),
        (0x00000003, 'loc_595'),
        (0x00000004, 'loc_5AC'),
        (0x00000006, 'loc_5C3'),
        (0x00000007, 'loc_5DA'),
        (0x00000008, 'loc_5F1'),
        (0x0000000A, 'loc_608'),
        (0x0000000E, 'loc_61F'),
        (0x0000000F, 'loc_636'),
        (-1, 'loc_64D'),
    )

    def _loc_57E(): pass

    label('loc_57E')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 9)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 10)

    Jump('loc_64D')

    def _loc_595(): pass

    label('loc_595')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 9)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 10)

    Jump('loc_64D')

    def _loc_5AC(): pass

    label('loc_5AC')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 9)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 10)

    Jump('loc_64D')

    def _loc_5C3(): pass

    label('loc_5C3')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 9)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 10)

    Jump('loc_64D')

    def _loc_5DA(): pass

    label('loc_5DA')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 9)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 10)

    Jump('loc_64D')

    def _loc_5F1(): pass

    label('loc_5F1')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 9)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 10)

    Jump('loc_64D')

    def _loc_608(): pass

    label('loc_608')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 9)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 10)

    Jump('loc_64D')

    def _loc_61F(): pass

    label('loc_61F')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 9)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 10)

    Jump('loc_64D')

    def _loc_636(): pass

    label('loc_636')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 9)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 10)

    Jump('loc_64D')

    def _loc_64D(): pass

    label('loc_64D')

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_67A'),
        (0x00000003, 'loc_691'),
        (0x00000004, 'loc_6A8'),
        (0x00000006, 'loc_6BF'),
        (0x00000007, 'loc_6D6'),
        (0x00000008, 'loc_6ED'),
        (0x0000000A, 'loc_704'),
        (0x0000000E, 'loc_71B'),
        (0x0000000F, 'loc_732'),
        (-1, 'loc_749'),
    )

    def _loc_67A(): pass

    label('loc_67A')

    LoadChip('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP', 9)
    LoadChip('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP', 10)

    Jump('loc_749')

    def _loc_691(): pass

    label('loc_691')

    LoadChip('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP', 9)
    LoadChip('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP', 10)

    Jump('loc_749')

    def _loc_6A8(): pass

    label('loc_6A8')

    LoadChip('ED6_DT27/CH04210._CH', 'ED6_DT27/CH04210P._CP', 9)
    LoadChip('ED6_DT27/CH04211._CH', 'ED6_DT27/CH04211P._CP', 10)

    Jump('loc_749')

    def _loc_6BF(): pass

    label('loc_6BF')

    LoadChip('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP', 9)
    LoadChip('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP', 10)

    Jump('loc_749')

    def _loc_6D6(): pass

    label('loc_6D6')

    LoadChip('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP', 9)
    LoadChip('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP', 10)

    Jump('loc_749')

    def _loc_6ED(): pass

    label('loc_6ED')

    LoadChip('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP', 9)
    LoadChip('ED6_DT27/CH04081._CH', 'ED6_DT27/CH04081P._CP', 10)

    Jump('loc_749')

    def _loc_704(): pass

    label('loc_704')

    LoadChip('ED6_DT07/CH00310._CH', 'ED6_DT07/CH00310P._CP', 9)
    LoadChip('ED6_DT07/CH00311._CH', 'ED6_DT07/CH00311P._CP', 10)

    Jump('loc_749')

    def _loc_71B(): pass

    label('loc_71B')

    LoadChip('ED6_DT27/CH04580._CH', 'ED6_DT27/CH04580P._CP', 9)
    LoadChip('ED6_DT27/CH04581._CH', 'ED6_DT27/CH04581P._CP', 10)

    Jump('loc_749')

    def _loc_732(): pass

    label('loc_732')

    LoadChip('ED6_DT27/CH04570._CH', 'ED6_DT27/CH04570P._CP', 9)
    LoadChip('ED6_DT27/CH04571._CH', 'ED6_DT27/CH04571P._CP', 10)

    Jump('loc_749')

    def _loc_749(): pass

    label('loc_749')

    LoadChip('ED6_DT27/CH04524._CH', 'ED6_DT27/CH04524P._CP', 11)
    LoadChip('ED6_DT27/CH04525._CH', 'ED6_DT27/CH04525P._CP', 12)
    LoadChip('ED6_DT27/CH04526._CH', 'ED6_DT27/CH04526P._CP', 13)
    LoadChip('ED6_DT29/CH12381._CH', 'ED6_DT29/CH12381P._CP', 14)
    LoadChip('ED6_DT09/CH10911._CH', 'ED6_DT09/CH10911P._CP', 15)
    LoadChip('ED6_DT26/CH20462._CH', 'ED6_DT26/CH20462P._CP', 16)
    LoadChip('ED6_DT26/CH20463._CH', 'ED6_DT26/CH20463P._CP', 17)

    Return()

# id: 0x0004 offset: 0x790
@scena.Code('func_04_790')
def func_04_790():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Call(0, 0x0002)
    CameraMove(-720, 0, -17580, 0)
    OP_67(0, 5710, -10000, 0)
    CameraSetDistance(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    CreateThread(0x0101, 0x00, 0x00, func_07_1319)
    Sleep(80)

    CreateThread(0x0102, 0x00, 0x00, func_08_133F)
    Sleep(50)

    CreateThread(0x00F8, 0x00, 0x00, func_09_1365)
    Sleep(100)

    CreateThread(0x00F9, 0x00, 0x00, func_0A_138B)

    @scena.Lambda('lambda_080E')
    def lambda_080E():
        CameraSetDistance(3960, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_080E)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    ChrSetChipByIndex(0x0008, 0)
    ChrSetPos(0x0008, 520, 0, 25630, 180)
    ChrClearFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0210410381V哎呀……\n',
            '预测有误吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000001F4)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_8DC',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_91A')

    def _loc_8DC(): pass

    label('loc_8DC')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_903',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_91A')

    def _loc_903(): pass

    label('loc_903')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_91A(): pass

    label('loc_91A')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_946',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_984')

    def _loc_946(): pass

    label('loc_946')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_96D',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_984')

    def _loc_96D(): pass

    label('loc_96D')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_984(): pass

    label('loc_984')

    Sleep(500)

    PlayBGM(111)
    Sleep(500)

    @scena.Lambda('lambda_0996')
    def lambda_0996():
        CameraMove(-550, 0, 26000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0996)

    @scena.Lambda('lambda_09AE')
    def lambda_09AE():
        OP_67(0, 4870, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09AE)

    @scena.Lambda('lambda_09C6')
    def lambda_09C6():
        CameraSetDistance(3290, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09C6)

    @scena.Lambda('lambda_09D6')
    def lambda_09D6():
        OP_6E(288, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_09D6)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetPos(0x0101, 1490, 0, 2610, 0)
    ChrSetPos(0x0102, 40, 0, 2660, 0)
    ChrSetPos(0x00F8, 1660, 0, 1390, 0)
    ChrSetPos(0x00F9, 260, 0, 1430, 0)

    ChrTalk(
        0x0101,
        (
            '#0010300854V#1020F#2P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410383V#1042F#5P『幻惑之铃』……是你吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A85')
    def lambda_0A85():
        CameraMove(-1500, 0, 22220, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0A85)

    @scena.Lambda('lambda_0A9D')
    def lambda_0A9D():
        OP_67(0, 4210, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A9D)

    @scena.Lambda('lambda_0AB5')
    def lambda_0AB5():
        CameraSetDistance(3400, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0AB5)

    @scena.Lambda('lambda_0AC5')
    def lambda_0AC5():
        OP_6E(292, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_0AC5)

    Sleep(1000)

    @scena.Lambda('lambda_0ADA')
    def lambda_0ADA():
        ChrWalkTo(0x00FE, 1350, 0, 16329, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0ADA)

    Sleep(80)

    @scena.Lambda('lambda_0AFA')
    def lambda_0AFA():
        ChrWalkTo(0x00FE, -250, 0, 16610, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0AFA)

    Sleep(100)

    @scena.Lambda('lambda_0B1A')
    def lambda_0B1A():
        ChrWalkTo(0x00FE, 1470, 0, 14860, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_0B1A)

    Sleep(40)

    ChrWalkTo(0x00F9, -40, 0, 14720, 6000, 0x00)
    WaitForThreadExit(0x0102, 0x0002)
    WaitForThreadExit(0x0101, 0x0002)

    ChrTalk(
        0x0008,
        (
            '#0210410384V#244F我还预感那丫头\n',
            '一定会来呢……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410385V#240F看来我的占卜还是不成熟呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410386V#1002F#6P……雪拉姐在\n',
            '埃尔赛尤上待命呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410387V#1042F#6P即使如此……\n',
            '你还是打算和我们战斗吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410388V#244F……是啊。\n',
            '我并没有帮助教授的义务，\n',
            '直接离开也是可以的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410389V#240F但说实话，没想到\n',
            '你们能打败布卢布兰和瓦鲁特\n',
            '来到这里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410390V你们究竟成长到了什么程度……\n',
            '我也想稍微见识一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 12)
    OP_0D()
    Sleep(500)

    ChrSetChipByIndex(0x0008, 13)

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

    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    OP_71(0x0000, 0x0004)
    CameraMove(0, 0, 24000, 0)
    OP_67(0, 3240, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(0, 0)
    OP_6E(347, 0)
    ChrSetPos(0x0008, 0, 0, 25600, 180)
    ChrSetPos(0x0101, 600, 0, 17580, 0)
    ChrSetPos(0x0102, -600, 0, 17580, 0)
    ChrSetPos(0x00F8, 1200, 0, 16000, 0)
    ChrSetPos(0x00F9, -1200, 0, 16000, 0)
    OP_0D()

    @scena.Lambda('lambda_0E00')
    def lambda_0E00():
        CameraSetDistance(3300, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0E00)

    LoadEffect(0x01, 'scraft\\sc040_08.eff')
    PlayEffect(0x01, 0x00, 0x00FF, 450, 0, 25660, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(613, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    StopEffect(0x00, 0x02)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    CreateThread(0x0009, 0x00, 0x00, func_05_120F)
    Sleep(800)

    CreateThread(0x000A, 0x00, 0x00, func_06_1294)
    Sleep(800)

    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x0102, 0x0002)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EFB',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_F39')

    def _loc_EFB(): pass

    label('loc_EFB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F22',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_F39')

    def _loc_F22(): pass

    label('loc_F22')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_F39(): pass

    label('loc_F39')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F65',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_FA3')

    def _loc_F65(): pass

    label('loc_F65')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F8C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_FA3')

    def _loc_F8C(): pass

    label('loc_F8C')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_FA3(): pass

    label('loc_FA3')

    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FE8',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410391V#178F<FIXME>……くっ……………！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FE8(): pass

    label('loc_FE8')

    Sleep(300)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)
    ChrSetChipByIndex(0x00F8, 7)
    ChrSetChipByIndex(0x00F9, 9)
    ChrSetSubChip(0x0000, 0)
    ChrSetSubChip(0x0001, 0)
    ChrSetSubChip(0x0002, 0)
    ChrSetSubChip(0x0003, 0)
    OP_0D()
    Sleep(300)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 12)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210410392V#244F#5P要是连我也无法打倒的话，\n',
            '你们就更没有可能\n',
            '通过上面的挑战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410393V#241F『幻惑之铃』的迷幻之舞……\n',
            '请拿出真本事来破解吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10D2')
    def lambda_10D2():
        CameraMove(0, 0, 24000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10D2)

    @scena.Lambda('lambda_10EA')
    def lambda_10EA():
        OP_67(0, 4610, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_10EA)

    @scena.Lambda('lambda_1102')
    def lambda_1102():
        CameraSetDistance(2600, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1102)

    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 1)

    @scena.Lambda('lambda_111C')
    def lambda_111C():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_111C)

    Sleep(30)

    ChrSetChipByIndex(0x0009, 15)
    ChrSetFlags(0x0009, 0x1000)

    @scena.Lambda('lambda_1146')
    def lambda_1146():
        ChrMoveToRelativeAsync(0x00FE, 1000, 0, -5000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_1146)

    @scena.Lambda('lambda_1161')
    def lambda_1161():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_1161)

    Sleep(30)

    ChrSetChipByIndex(0x000A, 14)
    ChrSetFlags(0x000A, 0x1000)

    @scena.Lambda('lambda_118B')
    def lambda_118B():
        ChrMoveToRelativeAsync(0x00FE, -1000, 0, -5000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_118B)

    @scena.Lambda('lambda_11A6')
    def lambda_11A6():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_11A6)

    @scena.Lambda('lambda_11C1')
    def lambda_11C1():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_11C1)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000462, 0x00000000, 0x00, 0x0000, 0xFF)
    Call(0, 0x000B)

    Return()

# id: 0x0005 offset: 0x120F
@scena.Code('func_05_120F')
def func_05_120F():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x00FE, 2)
    ChrSetPos(0x00FE, -2000, 2000, 26000, 180)
    ChrSetFlags(0x00FE, 0x0004)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_1240')
    def lambda_1240():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_1240')

    DispatchAsync2(0x00FE, 0x0003, lambda_1240)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_125D')
    def lambda_125D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_125D)

    @scena.Lambda('lambda_126F')
    def lambda_126F():
        ChrMoveTo(0x00FE, -2000, 500, 26000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_126F)

    WaitForThreadExit(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0002)
    PlaySE(538, 0x00, 0x64)

    Return()

# id: 0x0006 offset: 0x1294
@scena.Code('func_06_1294')
def func_06_1294():
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)
    ChrSetChipByIndex(0x00FE, 1)
    ChrSetPos(0x00FE, 2000, 2000, 26000, 180)
    ChrSetFlags(0x00FE, 0x0004)
    ChrClearFlags(0x00FE, 0x0080)

    @scena.Lambda('lambda_12C5')
    def lambda_12C5():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_12C5')

    DispatchAsync2(0x00FE, 0x0003, lambda_12C5)

    PlaySE(529, 0x00, 0x64)
    PlaySE(533, 0x00, 0x64)

    @scena.Lambda('lambda_12E2')
    def lambda_12E2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_12E2)

    @scena.Lambda('lambda_12F4')
    def lambda_12F4():
        ChrMoveTo(0x00FE, 2000, 500, 26000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_12F4)

    WaitForThreadExit(0x00FE, 0x0001)
    WaitForThreadExit(0x00FE, 0x0002)
    PlaySE(538, 0x00, 0x64)

    Return()

# id: 0x0007 offset: 0x1319
@scena.Code('func_07_1319')
def func_07_1319():
    ChrSetPos(0x00FE, 870, 0, -25040, 0)
    ChrWalkTo(0x00FE, 870, 0, -18040, 3000, 0x00)

    Return()

# id: 0x0008 offset: 0x133F
@scena.Code('func_08_133F')
def func_08_133F():
    ChrSetPos(0x00FE, -390, 0, -25050, 0)
    ChrWalkTo(0x00FE, -390, 0, -18050, 3000, 0x00)

    Return()

# id: 0x0009 offset: 0x1365
@scena.Code('func_09_1365')
def func_09_1365():
    ChrSetPos(0x00FE, 1150, 0, -26400, 0)
    ChrWalkTo(0x00FE, 1150, 0, -19400, 3000, 0x00)

    Return()

# id: 0x000A offset: 0x138B
@scena.Code('func_0A_138B')
def func_0A_138B():
    ChrSetPos(0x00FE, -210, 0, -26410, 0)
    ChrWalkTo(0x00FE, -210, 0, -19410, 3000, 0x00)

    Return()

# id: 0x000B offset: 0x13B1
@scena.Code('func_0B_13B1')
def func_0B_13B1():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    ChrSetPos(0x0101, 1000, 0, 19000, 0)
    ChrSetPos(0x0102, -460, 0, 19000, 0)
    ChrSetPos(0x00F8, 1510, 0, 17400, 0)
    ChrSetPos(0x00F9, -110, 0, 17400, 0)
    CameraMove(-970, 0, 23910, 0)
    OP_67(0, 4700, -10000, 0)
    CameraSetDistance(3330, 0)
    OP_6C(315000, 0)
    OP_6E(334, 0)
    ChrSetSubChip(0x0008, 3)
    ChrSetPos(0x0008, 520, 0, 26000, 180)
    ChrSetChipByIndex(0x0008, 11)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    FadeIn(1000, 0)
    CameraSetDistance(3130, 2000)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0210410455V#247F呵呵……原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410456V这样的话……说不定\n',
            '你们有资格继续向上层前进。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410457V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410458V#1040F#6P露茜奥拉……\n',
            '你愿意退下了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410459V#240F是啊……没有\n',
            '继续待在这里的理由了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0008, 0x03, 0x00, 1000)
    Fade(250)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 12)
    OP_0D()
    Sleep(500)

    ChrSetChipByIndex(0x0008, 13)

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

    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    @scena.Lambda('lambda_15D8')
    def lambda_15D8():
        CameraMove(-1400, 0, 24910, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_15D8)

    @scena.Lambda('lambda_15F0')
    def lambda_15F0():
        OP_67(0, 4000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_15F0)

    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 12)
    CreateThread(0x000B, 0x01, 0x00, func_0D_2149)
    CreateThread(0x000C, 0x01, 0x00, func_0E_21F9)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_167E',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_16BC')

    def _loc_167E(): pass

    label('loc_167E')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16A5',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_16BC')

    def _loc_16A5(): pass

    label('loc_16A5')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_16BC(): pass

    label('loc_16BC')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_16E8',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1726')

    def _loc_16E8(): pass

    label('loc_16E8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_170F',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_1726')

    def _loc_170F(): pass

    label('loc_170F')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_1726(): pass

    label('loc_1726')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010310663V#1020F#6P等、等一下！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410461V雪拉姐的事……\n',
            '你到底打算怎样！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410462V#247F#2P我与那丫头的因缘\n',
            '还没有了断……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410463V#240F所以，今后一定还会在\n',
            '某处重逢吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetRGBAMask(0x0008, 255, 255, 255, 90, 1000)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#0210410464V#244F#2P……话说回来，前方\n',
            '可是真正意义的死地哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410465V请你们做好准备后\n',
            '再慎重前进吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410466V#241F……那么祝你们顺利………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(286, 0x00, 0x64)

    @scena.Lambda('lambda_18A4')
    def lambda_18A4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_18A4)

    @scena.Lambda('lambda_18B6')
    def lambda_18B6():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 2000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_18B6)

    ChrSetRGBAMask(0x000C, 255, 255, 255, 0, 2000)
    Sleep(500)

    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)

    ChrTalk(
        0x0101,
        (
            '#0010410467V#1026F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410468V#1035F#6P……走了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1937')
    def lambda_1937():
        CameraMove(-820, 0, 20460, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1937)

    @scena.Lambda('lambda_194F')
    def lambda_194F():
        OP_67(0, 4700, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_194F)

    WaitForThreadExit(0x0101, 0x0001)
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
    Sleep(200)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A2A',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410469V#176F<FIXME>ふう……どうやら\n',
            '試されたようだな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410470V#170F悪人のようにも\n',
            '見受けられなかったが……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C47')

    def _loc_1A2A(): pass

    label('loc_1A2A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A7C',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410471V#071F#6P哎呀呀……\n',
            '倒也是个通情达理的好女人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C47')

    def _loc_1A7C(): pass

    label('loc_1A7C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1AC8',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410472V#031F#6P呼，不愧是身为\n',
            '雪拉的大姐的女人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C47')

    def _loc_1AC8(): pass

    label('loc_1AC8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B15',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410473V#1061F#6P怎么说呢……\n',
            '有成熟女性的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C47')

    def _loc_1B15(): pass

    label('loc_1B15')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1B5B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410474V#051F#6P嘿……\n',
            '很明白事理的女人嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C47')

    def _loc_1B5B(): pass

    label('loc_1B5B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BA1',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410475V#210F#6P嗯……\n',
            '有成熟女性的感觉呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C47')

    def _loc_1BA1(): pass

    label('loc_1BA1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1BE5',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410476V#1168F#6P这么通情理真是太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C47')

    def _loc_1BE5(): pass

    label('loc_1BE5')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C47',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410477V#066F<FIXME>えへへ、なんだか\n',
            '大人の女のひとって\n',
            '感じでしたよね……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C47(): pass

    label('loc_1C47')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CB0',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410478V#272F<FIXME>ふむ……\n',
            'しかし《銀閃》が知ったら\n',
            'さぞ気落ちするだろうな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F57')

    def _loc_1CB0(): pass

    label('loc_1CB0')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D02',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410479V#561F#6P但是，雪拉姐要是知道了\n',
            '会不会失望呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F57')

    def _loc_1D02(): pass

    label('loc_1D02')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D5B',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410480V#1169F#6P但是，雪拉扎德要是知道了，\n',
            '说不定会失望呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F57')

    def _loc_1D5B(): pass

    label('loc_1D5B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DAB',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410481V#215F#6P但是，那个甩鞭子的\n',
            '姐姐可能会失望呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F57')

    def _loc_1DAB(): pass

    label('loc_1DAB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1DFB',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410482V#551F#6P但是，雪拉扎德那家伙\n',
            '大概会很失望吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F57')

    def _loc_1DFB(): pass

    label('loc_1DFB')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1E43',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410483V#1068F但是雪拉姐\n',
            '不知道会不会失望啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F57')

    def _loc_1E43(): pass

    label('loc_1E43')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EF6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410484V#34F<FIXME>……ふむ、しかしシェラ君は\n',
            'ガッカリするかもしれないね。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040410485V#30F２人の間にも、\n',
            '２人にしか分からない絆が\n',
            'あったようだからね。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F57')

    def _loc_1EF6(): pass

    label('loc_1EF6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F57',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410486V#074F<FIXME>ふむ、しかしシェラザードは\n',
            'ガッカリするかもしれんな。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F57(): pass

    label('loc_1F57')

    ChrSetDirection(0x0101, -180, 400)
    Sleep(300)

    ChrTalk(
        0x0101,
        (
            '#0010410487V#1007F#2P<FIXME>うん……でも仕方ないよね。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410488V#1015Fあの２人が出会ったら\n',
            'それはそれで心配だったし……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 90, 400)
    Sleep(300)

    ChrTalk(
        0x0102,
        (
            '#0020410489V#1043F#5P也是……\n',
            '我想这也是一种缘分。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410490V#1035F虽然她从舞台上退场了，\n',
            '但我们的演出还未结束……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020410491V#1040F就按照她的忠告谨慎前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 270, 400)

    ChrTalk(
        0x0101,
        (
            '#0010410492V#1006F#4P……嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0446, 7, 0x2237))
    OP_72(0x0004, 0x0004)
    OP_28(0x009F, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x000C offset: 0x20D4
@scena.Code('func_0C_20D4')
def func_0C_20D4():
    @scena.Lambda('lambda_20DA')
    def lambda_20DA():
        ChrWalkTo(0x00FE, 850, 0, -17580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_20DA)

    Sleep(40)

    @scena.Lambda('lambda_20FA')
    def lambda_20FA():
        ChrWalkTo(0x00FE, -220, 0, -17550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_20FA)

    Sleep(100)

    @scena.Lambda('lambda_211A')
    def lambda_211A():
        ChrWalkTo(0x00FE, 1270, 0, -18810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0001, lambda_211A)

    Sleep(50)

    ChrWalkTo(0x00F9, -780, 0, -18730, 3000, 0x00)

    Return()

# id: 0x000D offset: 0x2149
@scena.Code('func_0D_2149')
def func_0D_2149():
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 12)
    ChrSetPos(0x000B, 520, 0, 26000, 180)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 90, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrMoveToRelativeAsync(0x000B, 50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, -50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, 100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, -100, 0, 0, 300, 0x00)
    def _loc_21C4(): pass

    label('loc_21C4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_21F8',
    )

    ChrMoveToRelativeAsync(0x000B, 150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000B, -150, 0, 0, 300, 0x00)

    Jump('loc_21C4')

    def _loc_21F8(): pass

    label('loc_21F8')

    Return()

# id: 0x000E offset: 0x21F9
@scena.Code('func_0E_21F9')
def func_0E_21F9():
    ChrSetSubChip(0x000C, 0)
    ChrSetChipByIndex(0x000C, 12)
    ChrSetPos(0x000C, 520, 0, 26000, 180)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 90, 0)
    ChrClearFlags(0x000C, 0x0080)
    ChrMoveToRelativeAsync(0x000C, -50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000C, 50, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000C, -100, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000C, 100, 0, 0, 300, 0x00)
    def _loc_2274(): pass

    label('loc_2274')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_22A8',
    )

    ChrMoveToRelativeAsync(0x000C, -150, 0, 0, 300, 0x00)
    ChrMoveToRelativeAsync(0x000C, 150, 0, 0, 300, 0x00)

    Jump('loc_2274')

    def _loc_22A8(): pass

    label('loc_22A8')

    Return()

# id: 0x000F offset: 0x22A9
@scena.Code('func_0F_22A9')
def func_0F_22A9():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    Call(0, 0x0003)
    CameraMove(-720, 0, -17580, 0)
    OP_67(0, 5710, -10000, 0)
    CameraSetDistance(4590, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    CreateThread(0x0101, 0x00, 0x00, func_07_1319)
    Sleep(80)

    CreateThread(0x0102, 0x00, 0x00, func_08_133F)
    Sleep(50)

    CreateThread(0x00F8, 0x00, 0x00, func_09_1365)
    Sleep(100)

    CreateThread(0x00F9, 0x00, 0x00, func_0A_138B)

    @scena.Lambda('lambda_2327')
    def lambda_2327():
        CameraSetDistance(3960, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2327)

    FadeIn(1000, 0)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x00F9, 0x0001)
    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23AD',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_23EB')

    def _loc_23AD(): pass

    label('loc_23AD')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_23D4',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_23EB')

    def _loc_23D4(): pass

    label('loc_23D4')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_23EB(): pass

    label('loc_23EB')

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2417',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2455')

    def _loc_2417(): pass

    label('loc_2417')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_243E',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_2455')

    def _loc_243E(): pass

    label('loc_243E')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_2455(): pass

    label('loc_2455')

    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2492',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410394V#172F<FIXME>鈴の音……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2492(): pass

    label('loc_2492')

    ChrSetChipByIndex(0x0008, 0)
    ChrSetPos(0x0008, 0, 0, 25630, 180)
    ChrClearFlags(0x0008, 0x0080)

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0210410395V呵呵……来得好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000001F4)
    OP_21()
    PlayBGM(111)
    Sleep(500)

    @scena.Lambda('lambda_24ED')
    def lambda_24ED():
        CameraMove(-550, 0, 26000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_24ED)

    @scena.Lambda('lambda_2505')
    def lambda_2505():
        OP_67(0, 4870, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2505)

    @scena.Lambda('lambda_251D')
    def lambda_251D():
        CameraSetDistance(3290, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_251D)

    @scena.Lambda('lambda_252D')
    def lambda_252D():
        OP_6E(288, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_252D)

    WaitForThreadExit(0x0101, 0x0000)
    ChrSetPos(0x0103, 330, 0, 350, 0)
    ChrSetPos(0x0101, 1300, 0, -1380, 0)
    ChrSetPos(0x0102, -100, 0, -1070, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2590',
    )

    ChrSetPos(0x00F9, 920, 0, -3120, 0)

    Jump('loc_25A1')

    def _loc_2590(): pass

    label('loc_2590')

    ChrSetPos(0x00F8, 920, 0, -3120, 0)

    def _loc_25A1(): pass

    label('loc_25A1')

    ChrTalk(
        0x0101,
        (
            '#0010300854V#1020F#2P啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410383V#1042F#5P『幻惑之铃』……是你吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_25FD')
    def lambda_25FD():
        CameraMove(-1300, 0, 22700, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_25FD)

    @scena.Lambda('lambda_2615')
    def lambda_2615():
        OP_67(0, 4210, -10000, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2615)

    @scena.Lambda('lambda_262D')
    def lambda_262D():
        CameraSetDistance(3480, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_262D)

    @scena.Lambda('lambda_263D')
    def lambda_263D():
        OP_6E(292, 4000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_263D)

    Sleep(1000)

    @scena.Lambda('lambda_2652')
    def lambda_2652():
        ChrWalkTo(0x00FE, 100, 0, 16970, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_2652)

    Sleep(80)

    @scena.Lambda('lambda_2672')
    def lambda_2672():
        ChrWalkTo(0x00FE, 2000, 0, 16000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2672)

    Sleep(150)

    @scena.Lambda('lambda_2692')
    def lambda_2692():
        ChrWalkTo(0x00FE, -200, 0, 15900, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2692)

    Sleep(40)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26D0',
    )

    ChrWalkTo(0x00F9, 1330, 0, 15000, 6000, 0x00)

    Jump('loc_26E4')

    def _loc_26D0(): pass

    label('loc_26D0')

    ChrWalkTo(0x00F8, 1330, 0, 15000, 6000, 0x00)

    def _loc_26E4(): pass

    label('loc_26E4')

    WaitForThreadExit(0x0102, 0x0002)
    WaitForThreadExit(0x0101, 0x0002)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030410398V#522F#6P露茜奥拉……姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410399V#244F竟能打败布卢布兰和瓦鲁特\n',
            '到达这里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410400V#240F你们还挺不赖的嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410401V#026F#6P姐姐……\n',
            '请履行约定吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410402V#022F你说再次见面时，\n',
            '会把哈维团长的事\n',
            '全部告诉我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410403V#241F啊啊……\n',
            '杀死他的理由吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410404V#522F#6P…………唔……………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410405V#244F这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410406V…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410407V#240F……我问你，雪拉扎德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410408V对你来说，\n',
            '团长是个怎样的人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410409V#024F#6P这、这\n',
            '还用说吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410410V当然是将身为孤儿的我\n',
            '收养培育的恩人啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(500, 0, -1)
    OP_0D()
    OP_AD('ED6_DT24/C_VIS104._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(1000)

    OP_AE(0x000001F4)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030410411V#524F#6P我虽然完全\n',
            '不知道父母的样子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410412V但是所谓的父亲大概\n',
            '就是这样的感觉吧。\n',
            '我一直是这么想的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410413V#527F……然而……\n',
            '然而为什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410414V#244F是啊……\n',
            '他是个温柔和蔼的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410415V#242F但是，身为旅行艺人的团长，\n',
            '只有温柔和蔼是行不通的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410416V从事肮脏的交易，把女艺人卖给客人\n',
            '这种事，在我们这个行业中屡见不鲜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410417V#244F但是团长……他却\n',
            '从没做过那种事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410418V因此他散尽了自己的全部财产……\n',
            '还背上了巨大的债务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030410419V#024F#6P骗、骗人吧……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410420V团长他…\n',
            '从来没有表现出那种……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410421V#240F呵呵，他人虽好，\n',
            '却非常要强。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410422V自然不会让我们察觉，\n',
            '独自一人到处奔走，筹调资金……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410423V#244F……而最后，\n',
            '他决定卖掉整个剧团。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410424V#023F#6P！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410425V#244F他打算把整个剧团\n',
            '都托付给一名认识的贵族。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410426V说什么如果自己继续当团长，\n',
            '我们就会永远贫苦下去……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410427V既然这样，还不如让可靠的人\n',
            '来照顾我们更好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410428V#240F……他大概就是这样的想法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410429V#522F#6P怎、怎么会……为什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410430V#024F要是他当时和我们商量的话，\n',
            '我们一定会全力帮忙的……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410431V#242F当他和我说明这一切时，\n',
            '我也是这样劝说他的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410432V但是，那个人太过顽固，\n',
            '完全听不进去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410433V#244F坚持认为自己太无能，\n',
            '对我们的前途没有任何好处……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410434V这样钻进了牛角尖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410435V#025F#6P………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410436V#522F就因为这个理由……\n',
            '……姐姐就把团长……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410437V#240F嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410438V对我来说，他这种决定\n',
            '完全就是难以容忍的背叛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410439V#244F将廉价的幸福和安逸给我们，\n',
            '却把更重要百倍的东西带走……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410440V要是这样的话，\n',
            '在一开始就不应该收留大家。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410441V#241F所以，我杀了他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410442V#522F#6P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410443V那样的话……\n',
            '……我又算是什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410444V#243F咦……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410445V#524F#6P我……全靠团长和姐姐\n',
            '才能得到安逸幸福的生活……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410446V在你们的照顾下，我拥有了在贫民街中\n',
            '从来没有得到过的温暖……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410447V#025F但是……团长死了……\n',
            '……连姐姐也离开了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410448V#527F这难道……\n',
            '……不是更残酷的背叛吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410449V#247F……呵呵，是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410450V#242F雪拉扎德。\n',
            '你有恨我的权利。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410451V带着那份恨意\n',
            '来和我一战吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 12)
    OP_0D()
    Sleep(500)

    ChrSetChipByIndex(0x0008, 13)

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

    PlaySE(280, 0x00, 0x64)
    Sleep(500)

    Fade(500)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    OP_71(0x0000, 0x0004)
    CameraMove(0, 0, 24000, 0)
    OP_67(0, 3240, -10000, 0)
    CameraSetDistance(2900, 0)
    OP_6C(0, 0)
    OP_6E(347, 0)
    ChrSetPos(0x0008, 0, 0, 25600, 180)
    ChrSetPos(0x0103, 40, 0, 18530, 0)
    ChrSetPos(0x0101, 950, 0, 17000, 0)
    ChrSetPos(0x0102, -950, 0, 17000, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3364',
    )

    ChrSetPos(0x00F9, 0, 0, 15040, 0)

    Jump('loc_3375')

    def _loc_3364(): pass

    label('loc_3364')

    ChrSetPos(0x00F8, 0, 0, 15040, 0)

    def _loc_3375(): pass

    label('loc_3375')

    OP_0D()

    @scena.Lambda('lambda_337C')
    def lambda_337C():
        CameraSetDistance(3300, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_337C)

    LoadEffect(0x01, 'scraft\\sc040_08.eff')
    PlayEffect(0x01, 0x00, 0x00FF, 450, 0, 25660, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(613, 0x00, 0x64)
    Sleep(1000)

    Fade(500)
    StopEffect(0x00, 0x02)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    CreateThread(0x0009, 0x00, 0x00, func_05_120F)
    Sleep(800)

    CreateThread(0x000A, 0x00, 0x00, func_06_1294)
    Sleep(800)

    WaitForThreadExit(0x0009, 0x0000)
    WaitForThreadExit(0x000A, 0x0000)
    WaitForThreadExit(0x0102, 0x0002)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34E1',
    )

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34A0',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_34DE')

    def _loc_34A0(): pass

    label('loc_34A0')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34C7',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_34DE')

    def _loc_34C7(): pass

    label('loc_34C7')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_34DE(): pass

    label('loc_34DE')

    Jump('loc_3546')

    def _loc_34E1(): pass

    label('loc_34E1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3508',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3546')

    def _loc_3508(): pass

    label('loc_3508')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_352F',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3546')

    def _loc_352F(): pass

    label('loc_352F')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_3546(): pass

    label('loc_3546')

    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030410452V#523F#6P姐姐……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410392V#244F#5P要是连我也无法打倒的话，\n',
            '你们就更没有可能\n',
            '通过上面的挑战。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410393V#241F『幻惑之铃』的迷幻之舞……\n',
            '请拿出真本事来破解吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(250)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x0101, 3)
    ChrSetChipByIndex(0x0102, 5)
    ChrSetChipByIndex(0x0103, 7)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_363A',
    )

    ChrSetChipByIndex(0x00F9, 9)

    Jump('loc_363F')

    def _loc_363A(): pass

    label('loc_363A')

    ChrSetChipByIndex(0x00F8, 9)

    def _loc_363F(): pass

    label('loc_363F')

    OP_0D()
    Sleep(500)

    @scena.Lambda('lambda_364B')
    def lambda_364B():
        CameraMove(0, 0, 24000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_364B)

    @scena.Lambda('lambda_3663')
    def lambda_3663():
        OP_67(0, 4610, -10000, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3663)

    @scena.Lambda('lambda_367B')
    def lambda_367B():
        CameraSetDistance(2600, 300)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_367B)

    ChrSetChipByIndex(0x0008, 13)
    ChrSetSubChip(0x0008, 1)

    @scena.Lambda('lambda_3695')
    def lambda_3695():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3695)

    Sleep(30)

    ChrSetChipByIndex(0x0009, 15)
    ChrSetFlags(0x0009, 0x1000)

    @scena.Lambda('lambda_36BF')
    def lambda_36BF():
        ChrMoveToRelativeAsync(0x00FE, 1000, 0, -5000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0000, lambda_36BF)

    @scena.Lambda('lambda_36DA')
    def lambda_36DA():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_36DA)

    Sleep(30)

    ChrSetChipByIndex(0x000A, 14)
    ChrSetFlags(0x000A, 0x1000)

    @scena.Lambda('lambda_3704')
    def lambda_3704():
        ChrMoveToRelativeAsync(0x00FE, -1000, 0, -5000, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0000, lambda_3704)

    @scena.Lambda('lambda_371F')
    def lambda_371F():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F8, 0x0000, lambda_371F)

    @scena.Lambda('lambda_373A')
    def lambda_373A():
        ChrMoveToRelativeAsync(0x00FE, 0, 0, 5000, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x00F9, 0x0000, lambda_373A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0003)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00F8, 0xFF)
    TerminateThread(0x00F9, 0xFF)
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x000A, 0xFF)
    Battle(0x00000462, 0x00000000, 0x00, 0x0000, 0xFF)
    Call(0, 0x0010)

    Return()

# id: 0x0010 offset: 0x3788
@scena.Code('func_10_3788')
def func_10_3788():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    TerminateThread(0x0009, 0x00)
    TerminateThread(0x000A, 0x00)
    TerminateThread(0x0101, 0x00)
    TerminateThread(0x0102, 0x00)
    TerminateThread(0x00F8, 0x00)
    TerminateThread(0x00F9, 0x00)
    Call(0, 0x0003)
    CameraMove(-4300, 0, 27440, 0)
    OP_67(0, 3170, -10000, 0)
    CameraSetDistance(3550, 0)
    OP_6C(315000, 0)
    OP_6E(317, 0)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x000A, 0x0080)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -5930, 0, 28960, 135)
    ChrSetPos(0x0103, -450, 0, 23490, 315)
    ChrSetPos(0x0101, 1530, 0, 22630, 315)
    ChrSetPos(0x0102, 320, 0, 21580, 315)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3861',
    )

    ChrSetPos(0x00F9, 2020, 0, 21130, 315)

    Jump('loc_3872')

    def _loc_3861(): pass

    label('loc_3861')

    ChrSetPos(0x00F8, 2020, 0, 21130, 315)

    def _loc_3872(): pass

    label('loc_3872')

    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetFlags(0x0008, 0x0002)
    ChrSetChipByIndex(0x0008, 16)
    ChrSetSubChip(0x0008, 0)
    FadeIn(1000, 0)
    CameraSetDistance(3350, 2000)
    OP_0D()

    ChrTalk(
        0x0008,
        (
            '#0210410493V#247F#5P呵呵……原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410494V#240F这样的话……或许你们\n',
            '有资格继续往上前进了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410495V#025F#6P……姐姐。\n',
            '有一点，我需要更正。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410496V#524F我并没有办法让\n',
            '自己憎恨姐姐。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410497V即使你离我而去，\n',
            '即使你杀害了团长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410498V#522F只是……\n',
            '我的心里好难过，好悲哀。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010291390V#1026F#4P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410500V#243F#5P……雪拉扎德………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410501V#025F#6P而且，我还是无法相信。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410502V#522F姐姐竟会为了这样的理由\n',
            '杀害了团长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410503V杀害了那个因为替我们着想\n',
            '才做了如此痛苦决定的团长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410504V#240F#5P…………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410505V#247F……呵呵……\n',
            '果然是瞒不过你吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()
    PlayBGM(83)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030410506V#022F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410507V#240F#5P刚才的话……还有下文。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410508V当我明白他的决心已经到了\n',
            '连我都无法说服的时候……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410509V#244F我便向他和盘托出了\n',
            '自己长久以来埋藏在心底的感情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410510V#023F#6P#3S！！！#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410511V姐姐……原来你对团长……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410512V#025F……原来……是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410513V#240F呵呵，他的年纪都能当我的父亲了，\n',
            '所以你应该是无法想象的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410514V所以……\n',
            '他的想法也是一样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410515V#244F虽然他把我当女儿一样地爱护，\n',
            '但是不可能会接受我的感情。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410516V他劝我不要为一时的感情所困，\n',
            '而应该去找一个合适的对象……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410517V#240F……对，他像说教一般地拒绝了我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410518V#522F#6P……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410519V#244F#5P虽然遭到拒绝很受打击，\n',
            '但对我来说，更为强烈的感觉却是恐惧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410520V为了不让我继续迷恋他……\n',
            '他竟然说要替我另寻良缘。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410521V#242F这时我已经完全意识到，\n',
            '这个人可能很快就要从我身边离开了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410522V#023F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3F11')
    def lambda_3F11():
        CameraSetDistance(3150, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3F11)

    ChrTalk(
        0x0008,
        (
            '#0210410523V#245F#5P……在我明白到这一点的一瞬间，\n',
            '我的内心响起了一个声音。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410524V#244F……不要让他离开我……\n',
            '要让他永远都属于我一个人……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410525V#241F于是我就顺从了那个声音……\n',
            '向他出手了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410526V#522F#6P……露茜奥拉……姐姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410527V#240F#5P我就是从那时开始\n',
            '才发现了自己内心的黑暗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410528V之后，在黑暗的引导下，\n',
            '……我接受了『噬身之蛇』的邀请……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410529V不知不觉之间……\n',
            '就走到了今天这一步。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410530V#247F呵呵，或许已经到了该落幕的时候吧。',
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
    ChrSetFlags(0x0008, 0x0040)

    @scena.Lambda('lambda_413B')
    def lambda_413B():
        CameraMove(-5000, 0, 28000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_413B)

    @scena.Lambda('lambda_4153')
    def lambda_4153():
        OP_67(0, 3470, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4153)

    ChrMoveTo(0x0008, -6550, 0, 29440, 1000, 0x00)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 17)
    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030410532V#024F#4S姐姐，不要！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x0008, 0x0004)

    @scena.Lambda('lambda_41F4')
    def lambda_41F4():
        CameraMove(-6300, 0, 29440, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_41F4)

    @scena.Lambda('lambda_420C')
    def lambda_420C():
        OP_67(0, 4170, -10000, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_420C)

    @scena.Lambda('lambda_4224')
    def lambda_4224():
        ChrMoveTo(0x00FE, -7110, -180, 30130, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4224)

    @scena.Lambda('lambda_423F')
    def lambda_423F():
        OP_99(0x00FE, 0x00, 0x07, 1500)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_423F)

    @scena.Lambda('lambda_424F')
    def lambda_424F():
        ChrWalkTo(0x00FE, -7110, -180, 30130, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_424F)

    FadeOut(1000, 0, -1)
    OP_0D()
    PlaySE(502, 0x00, 0x64)
    Sleep(3000)

    LoadChip('ED6_DT27/CH03005._CH', 'ED6_DT27/CH03005P._CP', 3)
    LoadChip('ED6_DT27/CH03015._CH', 'ED6_DT27/CH03015P._CP', 4)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42A8',
    )

    LoadChip('ED6_DT07/CH00055._CH', 'ED6_DT07/CH00055P._CP', 5)

    Jump('loc_437D')

    def _loc_42A8(): pass

    label('loc_42A8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42C3',
    )

    LoadChip('ED6_DT07/CH00035._CH', 'ED6_DT07/CH00035P._CP', 5)

    Jump('loc_437D')

    def _loc_42C3(): pass

    label('loc_42C3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42DE',
    )

    LoadChip('ED6_DT27/CH03215._CH', 'ED6_DT27/CH03215P._CP', 5)

    Jump('loc_437D')

    def _loc_42DE(): pass

    label('loc_42DE')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42F9',
    )

    LoadChip('ED6_DT07/CH00065._CH', 'ED6_DT07/CH00065P._CP', 5)

    Jump('loc_437D')

    def _loc_42F9(): pass

    label('loc_42F9')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4314',
    )

    LoadChip('ED6_DT07/CH00075._CH', 'ED6_DT07/CH00075P._CP', 5)

    Jump('loc_437D')

    def _loc_4314(): pass

    label('loc_4314')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_432F',
    )

    LoadChip('ED6_DT27/CH03085._CH', 'ED6_DT27/CH03085P._CP', 5)

    Jump('loc_437D')

    def _loc_432F(): pass

    label('loc_432F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_434A',
    )

    LoadChip('ED6_DT27/CH03103._CH', 'ED6_DT27/CH03103P._CP', 5)

    Jump('loc_437D')

    def _loc_434A(): pass

    label('loc_434A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4365',
    )

    LoadChip('ED6_DT27/CH03585._CH', 'ED6_DT27/CH03585P._CP', 5)

    Jump('loc_437D')

    def _loc_4365(): pass

    label('loc_4365')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_437D',
    )

    LoadChip('ED6_DT27/CH04574._CH', 'ED6_DT27/CH04574P._CP', 5)

    def _loc_437D(): pass

    label('loc_437D')

    LoadChip('ED6_DT07/CH00025._CH', 'ED6_DT07/CH00025P._CP', 6)
    LoadChip('ED6_DT26/CH20464._CH', 'ED6_DT26/CH20464P._CP', 11)
    LoadChip('ED6_DT26/CH20465._CH', 'ED6_DT26/CH20465P._CP', 12)
    OP_71(0x0000, 0x0004)
    OP_72(0x0001, 0x0004)
    CameraMove(-8950, -8350, 31840, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(1480, 0)
    OP_6C(90000, 0)
    OP_6E(500, 0)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    ChrClearFlags(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0004)
    ChrSetFlags(0x0008, 0x0002)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetSubChip(0x0008, 0)
    ChrSetChipByIndex(0x0008, 12)
    ChrSetFlags(0x0103, 0x0002)
    ChrSetSubChip(0x0103, 0)
    ChrSetChipByIndex(0x0103, 11)
    ChrSetPos(0x0103, -8900, -1500, 31650, 0)
    ChrSetPos(0x0008, -9000, -6000, 32030, 0)

    @scena.Lambda('lambda_4445')
    def lambda_4445():
        OP_99(0x00FE, 0x00, 0x07, 1500)
        Yield()

        Jump('lambda_4445')

    DispatchAsync2(0x0008, 0x0002, lambda_4445)

    ChrSetPos(0x000E, -8900, -2100, 31650, 0)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_4472')
    def lambda_4472():
        CameraMove(-8950, -3200, 31840, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4472)

    @scena.Lambda('lambda_448A')
    def lambda_448A():
        OP_67(0, 7000, -10000, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_448A)

    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0030410533V#522F#5P唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410534V#247F呵呵……你的鞭术\n',
            '也大有进步呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410535V刚开始的时候\n',
            '是那么地拙笨呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetPos(0x0101, -2900, 0, 28690, 315)
    ChrSetPos(0x0102, -3920, 0, 27230, 315)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_456A',
    )

    ChrSetPos(0x00F9, -2360, 0, 27210, 315)

    Jump('loc_457B')

    def _loc_456A(): pass

    label('loc_456A')

    ChrSetPos(0x00F8, -2360, 0, 27210, 315)

    def _loc_457B(): pass

    label('loc_457B')

    ChrTalk(
        0x0101,
        (
            '#0010410536V#3P雪拉姐！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    @scena.Lambda('lambda_45A3')
    def lambda_45A3():
        CameraMove(-8950, -3000, 31840, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_45A3)

    @scena.Lambda('lambda_45BB')
    def lambda_45BB():
        OP_67(0, 7800, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_45BB)

    CreateThread(0x0101, 0x01, 0x00, func_12_544F)
    Sleep(500)

    CreateThread(0x0102, 0x01, 0x00, func_13_5475)
    Sleep(300)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_45FC',
    )

    CreateThread(0x00F9, 0x01, 0x00, func_14_5494)

    Jump('loc_4603')

    def _loc_45FC(): pass

    label('loc_45FC')

    CreateThread(0x00F8, 0x01, 0x00, func_14_5494)

    def _loc_4603(): pass

    label('loc_4603')

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#0210410537V#242F艾丝蒂尔、约修亚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410538V给我一点点时间就好……\n',
            '就让我这样子再和这孩子说几句话吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410539V#1020F#3P可、可是……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410540V#1043F#4P露茜奥拉……你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030410541V#523F#5P现、现在可不是\n',
            '说话的时候吧！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410542V抓紧了，我拉你上来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_473B')
    def lambda_473B():
        CameraSetDistance(1350, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_473B)

    ChrTalk(
        0x0008,
        (
            '#0210410543V#247F呵呵，雪拉扎德……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410544V直到现在，我都没有\n',
            '后悔过对他下手……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410545V但我唯一不能释怀的，\n',
            '就是从你的身边离开。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410546V在我离开后，你过得好不好…\n',
            '这件事一直都是我心底的牵挂。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410547V#240F不过，即便没有我在你的身边，\n',
            '你也仍然成长了不少呢，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410548V而且也找到了属于自己的道路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#0030410549V#522F#5P姐姐……求求你……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410550V#246F只要能够确认到这一点，\n',
            '我也就算没有白来利贝尔。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410551V其实，我本来是想让你亲手\n',
            '对我的过错进行惩罚和制裁的…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410552V可是……\n',
            '那果然只是我一厢情愿的想法罢了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(
        0x000E,
        (
            '#0030410553V#527F#5P……求求你！！\n',
            '好好抓紧啊！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 500, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0210410554V#247F呵呵，喝酒我不反对……\n',
            '……不过可要有节制哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0210410555V别了……我的雪拉扎德。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapClearFlags(0x00000010)

    @scena.Lambda('lambda_4A44')
    def lambda_4A44():
        CameraSetDistance(1200, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4A44)

    TerminateThread(0x0008, 0x02)
    ChrSetSubChip(0x0008, 32)

    @scena.Lambda('lambda_4A5D')
    def lambda_4A5D():
        OP_99(0x00FE, 0x20, 0x2A, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_4A5D)

    Sleep(100)

    PlaySE(550, 0x00, 0x64)
    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_4A7C')
    def lambda_4A7C():
        CameraMove(-12950, -5000, 31840, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_4A7C)

    @scena.Lambda('lambda_4A94')
    def lambda_4A94():
        OP_67(0, 14000, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_4A94)

    @scena.Lambda('lambda_4AAC')
    def lambda_4AAC():
        CameraSetDistance(1000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4AAC)

    ChrSetFlags(0x0008, 0x0020)
    CreateThread(0x0008, 0x01, 0x00, func_15_54BA)
    OP_99(0x0008, 0x2A, 0x2F, 2000)

    @scena.Lambda('lambda_4AD1')
    def lambda_4AD1():
        OP_99(0x00FE, 0x30, 0x37, 2000)
        Yield()

        Jump('lambda_4AD1')

    DispatchAsync2(0x0008, 0x0003, lambda_4AD1)

    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030410556V#20A#6P#4S露茜奥拉姐姐——！！！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(1000)

    FadeOut(1000, 0, -1)
    OP_0D()

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    MapSetFlags(0x00000010)
    Sleep(1000)

    ChrSetFlags(0x0008, 0x0080)
    PlaySE(286, 0x00, 0x46)
    Sleep(3000)

    OP_72(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    CameraMove(-5370, 0, 28490, 0)
    OP_67(0, 6130, -10000, 0)
    CameraSetDistance(3420, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrClearFlags(0x0103, 0x0002)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x00F8, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetChipByIndex(0x0103, 6)
    ChrSetPos(0x0103, -6060, 0, 29160, 315)
    ChrSetPos(0x0101, -3810, 0, 26970, 315)
    ChrSetPos(0x0102, -4800, 0, 26550, 315)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4C00',
    )

    ChrSetPos(0x00F9, -3310, 0, 27830, 315)

    Jump('loc_4C11')

    def _loc_4C00(): pass

    label('loc_4C00')

    ChrSetPos(0x00F8, -3310, 0, 27830, 315)

    def _loc_4C11(): pass

    label('loc_4C11')

    FadeIn(2000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030400882V#522F…………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410558V#1026F雪、雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341396V#1043F#6P雪拉姐……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410560V#026F…………没事了………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0103, 65535)
    OP_0D()
    Sleep(500)

    ChrSetDirection(0x0103, 135, 400)
    Sleep(500)

    ChrTalk(
        0x0103,
        (
            '#0030410561V#524F……姐姐她\n',
            '一定不会这么容易就摔死的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410562V总有一天，一定能……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410563V……一定能……再见面的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410564V#1025F嗯、嗯……一定会的！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410565V她会使用那么厉害的式神\n',
            '和幻术呢！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410566V绝对……\n',
            '……绝对没问题的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030410567V#021F呵呵……是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410568V#524F…………………………………',
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
        'loc_4EA6',
    )

    ChrTalk(
        0x0104,
        (
            '#0040410569V#032F雪拉……\n',
            '别太勉强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040410570V还是先回埃尔赛尤吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F7')

    def _loc_4EA6(): pass

    label('loc_4EA6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F0B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050410571V#555F雪拉扎德……\n',
            '别太勉强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050410572V还是先回埃尔赛尤吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F7')

    def _loc_4F0B(): pass

    label('loc_4F0B')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4F70',
    )

    ChrTalk(
        0x0108,
        (
            '#0080410573V#572F雪拉扎德……\n',
            '别太勉强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080410574V还是先回埃尔赛尤吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F7')

    def _loc_4F70(): pass

    label('loc_4F70')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['凯文神父'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4FD1',
    )

    ChrTalk(
        0x0109,
        (
            '#0180410575V#1067F大姐……别太勉强了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0180410576V还是先回埃尔赛尤吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F7')

    def _loc_4FD1(): pass

    label('loc_4FD1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5041',
    )

    ChrTalk(
        0x0105,
        (
            '#0060410577V#1163F雪拉扎德小姐……\n',
            '请不要太勉强自己。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060410578V还是先回埃尔赛尤吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F7')

    def _loc_5041(): pass

    label('loc_5041')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_50B2',
    )

    ChrTalk(
        0x0107,
        (
            '#0070410579V#063F那个，雪拉姐姐……\n',
            '不要太勉强自己……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070410580V还是先回埃尔赛尤吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F7')

    def _loc_50B2(): pass

    label('loc_50B2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['尤莉亚上尉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_5128',
    )

    ChrTalk(
        0x010F,
        (
            '#0100410581V#175F<FIXME>シェラザード君……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100410582Vここは一度、\n',
            'アルセイユに戻った方が……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F7')

    def _loc_5128(): pass

    label('loc_5128')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['乔丝特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_518D',
    )

    ChrTalk(
        0x010B,
        (
            '#0090410583V#212F我说……\n',
            '太勉强自己可不好哦？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0090410584V还是先回船上吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51F7')

    def _loc_518D(): pass

    label('loc_518D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['穆拉'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_51F7',
    )

    ChrTalk(
        0x0110,
        (
            '#0110410585V#276F……無理をするな。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0110410586V一度船に戻って\n',
            '休んだ方がいいだろう。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51F7(): pass

    label('loc_51F7')

    ChrTalk(
        0x0103,
        (
            '#0030410587V#026F不……没那个必要。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410588V……如果这样就气馁的话，\n',
            '姐姐会笑话我的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030410589V#020F所以，我们现在继续前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010410590V#1004F雪拉姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010410591V#1025F嗯……明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020410592V#1035F#6P那么……\n',
            '解除终端吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000003E8)
    FadeOut(1000, 0, -1)
    OP_0D()
    OP_21()
    CameraMove(-2420, 0, 25750, 0)
    OP_67(0, 6500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, -2420, 0, 25750, 0)
    ChrSetPos(0x0001, -2420, 0, 25750, 0)
    ChrSetPos(0x0002, -2420, 0, 25750, 0)
    ChrSetPos(0x0003, -2420, 0, 25750, 0)
    PlayBGM(64)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x40),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Sleep(500)

    FadeIn(1000, 0)
    SetScenaFlags(ScenaFlag(0x0447, 0, 0x2238))
    OP_72(0x0004, 0x0004)
    OP_28(0x009F, 0x01, 0x0100)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x53B6
@scena.Code('func_11_53B6')
def func_11_53B6():
    @scena.Lambda('lambda_53BC')
    def lambda_53BC():
        ChrWalkTo(0x00FE, 850, 0, -17580, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_53BC)

    Sleep(40)

    @scena.Lambda('lambda_53DC')
    def lambda_53DC():
        ChrWalkTo(0x00FE, -220, 0, -17550, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0001, lambda_53DC)

    Sleep(100)

    @scena.Lambda('lambda_53FC')
    def lambda_53FC():
        ChrWalkTo(0x00FE, 1270, 0, -18810, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_53FC)

    Sleep(50)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_543A',
    )

    ChrWalkTo(0x00F9, -780, 0, -18730, 3000, 0x00)

    Jump('loc_544E')

    def _loc_543A(): pass

    label('loc_543A')

    ChrWalkTo(0x00F8, -780, 0, -18730, 3000, 0x00)

    def _loc_544E(): pass

    label('loc_544E')

    Return()

# id: 0x0012 offset: 0x544F
@scena.Code('func_12_544F')
def func_12_544F():
    ChrWalkTo(0x00FE, -8130, -1500, 32430, 5000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 3)

    Return()

# id: 0x0013 offset: 0x5475
@scena.Code('func_13_5475')
def func_13_5475():
    ChrWalkTo(0x00FE, -8950, -1500, 30520, 5000, 0x00)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 4)

    Return()

# id: 0x0014 offset: 0x5494
@scena.Code('func_14_5494')
def func_14_5494():
    ChrWalkTo(0x00FE, -7690, -1500, 31770, 5000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    ChrSetSubChip(0x00FE, 0)
    ChrSetChipByIndex(0x00FE, 5)

    Return()

# id: 0x0015 offset: 0x54BA
@scena.Code('func_15_54BA')
def func_15_54BA():
    @scena.Lambda('lambda_54C0')
    def lambda_54C0():
        ChrMoveToRelativeAsync(0x00FE, 0, -20000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_54C0)

    Sleep(500)

    @scena.Lambda('lambda_54E0')
    def lambda_54E0():
        ChrMoveToRelativeAsync(0x00FE, 0, -20000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_54E0)

    Sleep(500)

    @scena.Lambda('lambda_5500')
    def lambda_5500():
        ChrMoveToRelativeAsync(0x00FE, 0, -20000, 0, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0002, lambda_5500)

    Return()

# id: 0x0016 offset: 0x5516
@scena.Code('func_16_5516')
def func_16_5516():
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '通往上层区域方向的隔离壁，\n',
            '以及传送门的锁定解除。',
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
    NewScene('ED6_DT21/C5305._SN', 115, 0, 0)
    IdleLoop()

    Return()

# id: 0x0017 offset: 0x5584
@scena.Code('func_17_5584')
def func_17_5584():
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
        'loc_559B',
    )

    Call(0, 0x0019)
    Call(0, 0x001A)

    def _loc_559B(): pass

    label('loc_559B')

    CameraMove(-800, 0, 33180, 0)
    OP_67(0, 5170, -10000, 0)
    CameraSetDistance(3520, 0)
    OP_6C(327000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 700, 0, 31480, 0)
    ChrSetPos(0x0102, -170, 0, 31400, 0)
    ChrSetPos(0x00F8, 1210, 0, 29860, 0)
    ChrSetPos(0x00F9, 70, 0, 29750, 0)
    FadeIn(1000, 0)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('声音')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '向上层区域方向的隔离壁，\n',
            '以及传送门的锁定已经解除了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    Fade(500)
    OP_71(0x0002, 0x0004)
    OP_0D()
    Sleep(500)

    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x0447, 1, 0x2239))
    OP_28(0x009F, 0x01, 0x0200)
    EventEnd(0x00)

    Return()

# id: 0x0018 offset: 0x569B
@scena.Code('func_18_569B')
def func_18_569B():
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
        'loc_56B2',
    )

    Call(0, 0x0019)
    Call(0, 0x001A)

    def _loc_56B2(): pass

    label('loc_56B2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_56C7',
    )

    Call(0, 0x0004)

    Jump('loc_56CB')

    def _loc_56C7(): pass

    label('loc_56C7')

    Call(0, 0x000F)

    def _loc_56CB(): pass

    label('loc_56CB')

    Return()

# id: 0x0019 offset: 0x56CC
@scena.Code('func_19_56CC')
def func_19_56CC():
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
        (0x00000000, 'loc_5746'),
        (0x00000001, 'loc_574C'),
        (-1, 'loc_5752'),
    )

    def _loc_5746(): pass

    label('loc_5746')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_5752')

    def _loc_574C(): pass

    label('loc_574C')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_5752')

    def _loc_5752(): pass

    label('loc_5752')

    Return()

# id: 0x001A offset: 0x5753
@scena.Code('func_1A_5753')
def func_1A_5753():
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

# id: 0x001B offset: 0x57E6
@scena.Code('func_1B_57E6')
def func_1B_57E6():
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
