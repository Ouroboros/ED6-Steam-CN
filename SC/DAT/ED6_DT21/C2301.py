import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2301   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2301.x'
    header.mapIndex       = 1
    header.bgm            = 60
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
        ('ED6_DT29/CH12730._CH', 'ED6_DT29/CH12730P._CP'),
        ('ED6_DT29/CH12731._CH', 'ED6_DT29/CH12731P._CP'),
        ('ED6_DT29/CH12740._CH', 'ED6_DT29/CH12740P._CP'),
        ('ED6_DT29/CH12741._CH', 'ED6_DT29/CH12741P._CP'),
        ('ED6_DT29/CH12750._CH', 'ED6_DT29/CH12750P._CP'),
        ('ED6_DT29/CH12751._CH', 'ED6_DT29/CH12751P._CP'),
        ('ED6_DT29/CH12760._CH', 'ED6_DT29/CH12760P._CP'),
        ('ED6_DT29/CH12761._CH', 'ED6_DT29/CH12761P._CP'),
        ('ED6_DT29/CH12770._CH', 'ED6_DT29/CH12770P._CP'),
        ('ED6_DT29/CH12771._CH', 'ED6_DT29/CH12771P._CP'),
        ('ED6_DT29/CH12780._CH', 'ED6_DT29/CH12780P._CP'),
        ('ED6_DT29/CH12781._CH', 'ED6_DT29/CH12781P._CP'),
        ('ED6_DT29/CH12790._CH', 'ED6_DT29/CH12790P._CP'),
        ('ED6_DT29/CH12791._CH', 'ED6_DT29/CH12791P._CP'),
        ('ED6_DT27/CH04000._CH', 'ED6_DT27/CH04000P._CP'),
        ('ED6_DT27/CH04010._CH', 'ED6_DT27/CH04010P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT27/CH04080._CH', 'ED6_DT27/CH04080P._CP'),
    ]

# id: 0x10001 offset: 0x15A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '守护者',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x17A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -4440,
            z           = 400,
            y           = -40370,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0401,
            word_18     = 0x1E9E,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 4560,
            z           = 400,
            y           = -40400,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0401,
            word_18     = 0x1E9F,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 350,
            z           = 200,
            y           = -7490,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1EA0,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 310,
            z           = 50,
            y           = 8930,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0404,
            word_18     = 0x1EA1,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 510,
            z           = 0,
            y           = 370,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0400,
            word_18     = 0x1EA2,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x206
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -4000,
            y           = 0,
            z           = 29000,
            range       = 4000,
            dword_10    = 0x00000BB8,
            dword_14    = 0x00007EFD,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10004 offset: 0x226
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -5380,
            triggerZ            = 400,
            triggerY            = -9620,
            triggerRange        = 1000,
            actorX              = -5850,
            actorZ              = 400,
            actorY              = -10080,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5300,
            triggerZ            = 400,
            triggerY            = -110,
            triggerRange        = 1000,
            actorX              = -5980,
            actorZ              = 400,
            actorY              = -50,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5470,
            triggerZ            = 400,
            triggerY            = 11520,
            triggerRange        = 1000,
            actorX              = -5880,
            actorZ              = 400,
            actorY              = 11930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5580,
            triggerZ            = 400,
            triggerY            = 11420,
            triggerRange        = 1000,
            actorX              = 6050,
            actorZ              = 400,
            actorY              = 11880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5280,
            triggerZ            = 400,
            triggerY            = 300,
            triggerRange        = 1000,
            actorX              = 5970,
            actorZ              = 400,
            actorY              = 50,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 5470,
            triggerZ            = 400,
            triggerY            = -9530,
            triggerRange        = 1000,
            actorX              = 6030,
            actorZ              = 400,
            actorY              = -10090,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 0,
            triggerZ            = 0,
            triggerY            = 38890,
            triggerRange        = 1000,
            actorX              = 0,
            actorZ              = 0,
            actorY              = 38890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000E,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x322
@scena.Code('Init')
def Init():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_332'),
        (0x00000065, 'loc_339'),
        (-1, 'loc_340'),
    )

    def _loc_332(): pass

    label('loc_332')

    Event(0, func_11_1A04)

    Jump('loc_340')

    def _loc_339(): pass

    label('loc_339')

    Event(0, func_13_1B92)

    Jump('loc_340')

    def _loc_340(): pass

    label('loc_340')

    Return()

# id: 0x0001 offset: 0x341
@scena.Code('func_01_341')
def func_01_341():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 0, 0x1F70)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_353',
    )

    OP_6F(0x0008, 0)

    Jump('loc_35A')

    def _loc_353(): pass

    label('loc_353')

    OP_6F(0x0008, 60)

    def _loc_35A(): pass

    label('loc_35A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 1, 0x1F71)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36C',
    )

    OP_6F(0x0009, 0)

    Jump('loc_373')

    def _loc_36C(): pass

    label('loc_36C')

    OP_6F(0x0009, 60)

    def _loc_373(): pass

    label('loc_373')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 2, 0x1F72)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_385',
    )

    OP_6F(0x000A, 0)

    Jump('loc_38C')

    def _loc_385(): pass

    label('loc_385')

    OP_6F(0x000A, 60)

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 3, 0x1F73)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_39E',
    )

    OP_6F(0x000B, 0)

    Jump('loc_3A5')

    def _loc_39E(): pass

    label('loc_39E')

    OP_6F(0x000B, 60)

    def _loc_3A5(): pass

    label('loc_3A5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 4, 0x1F74)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3B7',
    )

    OP_6F(0x000C, 0)

    Jump('loc_3BE')

    def _loc_3B7(): pass

    label('loc_3B7')

    OP_6F(0x000C, 60)

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 5, 0x1F75)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D0',
    )

    OP_6F(0x000D, 0)

    Jump('loc_3D7')

    def _loc_3D0(): pass

    label('loc_3D0')

    OP_6F(0x000D, 60)

    def _loc_3D7(): pass

    label('loc_3D7')

    OP_E0(0x08, 0x60, 0xEB, 0xFF, 0xFF, 0x90, 0x01, 0x00, 0x00, 0x08, 0xDA, 0xFF, 0xFF)
    OP_E0(0x0A, 0x06, 0xEB, 0xFF, 0xFF, 0x90, 0x01, 0x00, 0x00, 0x9C, 0x2C, 0x00, 0x00)
    OP_E0(0x0B, 0x68, 0x15, 0x00, 0x00, 0x90, 0x01, 0x00, 0x00, 0x38, 0x2C, 0x00, 0x00)
    OP_E0(0x0D, 0xFA, 0x14, 0x00, 0x00, 0x90, 0x01, 0x00, 0x00, 0x2A, 0xDB, 0xFF, 0xFF)
    LoadEffect(0x00, 'map\\\\mp049_21.eff')
    LoadEffect(0x01, 'map\\\\mp049_22.eff')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D3, 6, 0x1E9E)),
            Expr.Return,
        ),
        'loc_443',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_443(): pass

    label('loc_443')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D3, 7, 0x1E9F)),
            Expr.Return,
        ),
        'loc_44F',
    )

    ChrSetFlags(0x000A, 0x0080)

    def _loc_44F(): pass

    label('loc_44F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D4, 0, 0x1EA0)),
            Expr.Return,
        ),
        'loc_45B',
    )

    ChrSetFlags(0x000B, 0x0080)

    def _loc_45B(): pass

    label('loc_45B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D4, 1, 0x1EA1)),
            Expr.Return,
        ),
        'loc_467',
    )

    ChrSetFlags(0x000C, 0x0080)

    def _loc_467(): pass

    label('loc_467')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03D4, 2, 0x1EA2)),
            Expr.Return,
        ),
        'loc_473',
    )

    ChrSetFlags(0x000D, 0x0080)

    def _loc_473(): pass

    label('loc_473')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 3, 0x1E1B)),
            Expr.Return,
        ),
        'loc_505',
    )

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)

    Jump('loc_58D')

    def _loc_505(): pass

    label('loc_505')

    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_72(0x0003, 0x0020)
    OP_72(0x0004, 0x0020)
    OP_72(0x0005, 0x0020)
    OP_72(0x0006, 0x0020)
    OP_72(0x0007, 0x0020)
    OP_72(0x0000, 0x0008)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0008)
    OP_72(0x0003, 0x0008)
    OP_72(0x0004, 0x0008)
    OP_72(0x0005, 0x0008)
    OP_72(0x0006, 0x0008)
    OP_72(0x0007, 0x0008)
    OP_6F(0x0000, 0)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)

    def _loc_58D(): pass

    label('loc_58D')

    OP_1B(0x00, 0x00, 0x0012)
    OP_1B(0x01, 0x00, 0x0014)

    Return()

# id: 0x0002 offset: 0x598
@scena.Code('func_02_598')
def func_02_598():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_5AD',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_598')

    def _loc_5AD(): pass

    label('loc_5AD')

    Return()

# id: 0x0003 offset: 0x5AE
@scena.Code('func_03_5AE')
def func_03_5AE():
    UnlockAchievement(0x02, 0x008E, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 0, 0x1F70)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_68B',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0008, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['大回复药'], 1)"),
            Expr.Return,
        ),
        'loc_622',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EE, 0, 0x1F70))

    Jump('loc_688')

    def _loc_622(): pass

    label('loc_622')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['大回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0008, 60)
    OP_70(0x0008, 0)

    def _loc_688(): pass

    label('loc_688')

    Jump('loc_6BC')

    def _loc_68B(): pass

    label('loc_68B')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_6BC(): pass

    label('loc_6BC')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x6CA
@scena.Code('func_04_6CA')
def func_04_6CA():
    UnlockAchievement(0x02, 0x008F, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 1, 0x1F71)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7A7',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0009, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_73E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EE, 1, 0x1F71))

    Jump('loc_7A4')

    def _loc_73E(): pass

    label('loc_73E')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['圣灵药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0009, 60)
    OP_70(0x0009, 0)

    def _loc_7A4(): pass

    label('loc_7A4')

    Jump('loc_7D8')

    def _loc_7A7(): pass

    label('loc_7A7')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_7D8(): pass

    label('loc_7D8')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x7E6
@scena.Code('func_05_7E6')
def func_05_7E6():
    UnlockAchievement(0x02, 0x0090, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 2, 0x1F72)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8C3',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000A, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['清醒之药'], 1)"),
            Expr.Return,
        ),
        'loc_85A',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EE, 2, 0x1F72))

    Jump('loc_8C0')

    def _loc_85A(): pass

    label('loc_85A')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['清醒之药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000A, 60)
    OP_70(0x000A, 0)

    def _loc_8C0(): pass

    label('loc_8C0')

    Jump('loc_8F4')

    def _loc_8C3(): pass

    label('loc_8C3')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_8F4(): pass

    label('loc_8F4')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x902
@scena.Code('func_06_902')
def func_06_902():
    UnlockAchievement(0x02, 0x0091, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 3, 0x1F73)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_9DF',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000B, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['EP填充剂Ⅰ'], 1)"),
            Expr.Return,
        ),
        'loc_976',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EE, 3, 0x1F73))

    Jump('loc_9DC')

    def _loc_976(): pass

    label('loc_976')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['EP填充剂Ⅰ']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000B, 60)
    OP_70(0x000B, 0)

    def _loc_9DC(): pass

    label('loc_9DC')

    Jump('loc_A10')

    def _loc_9DF(): pass

    label('loc_9DF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_A10(): pass

    label('loc_A10')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0xA1E
@scena.Code('func_07_A1E')
def func_07_A1E():
    UnlockAchievement(0x02, 0x0092, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 4, 0x1F74)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_AFB',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000C, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['绝缘胶带'], 1)"),
            Expr.Return,
        ),
        'loc_A92',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x03EE, 4, 0x1F74))

    Jump('loc_AF8')

    def _loc_A92(): pass

    label('loc_A92')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['绝缘胶带']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x000C, 60)
    OP_70(0x000C, 0)

    def _loc_AF8(): pass

    label('loc_AF8')

    Jump('loc_B2C')

    def _loc_AFB(): pass

    label('loc_AFB')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    def _loc_B2C(): pass

    label('loc_B2C')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0008 offset: 0xB3A
@scena.Code('func_08_B3A')
def func_08_B3A():
    UnlockAchievement(0x02, 0x0093, 0x00)
    MapSetFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03EE, 5, 0x1F75)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C0F',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x000D, 30)
    OP_73(0x000D)
    OP_6F(0x000D, 30)
    AddSepith(0x01, 300)
    AddSepith(0x04, 100)
    AddSepith(0x05, 100)
    AddSepith(0x06, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×３００\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×１００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    SetScenaFlags(ScenaFlag(0x03EE, 5, 0x1F75))

    Jump('loc_C29')

    def _loc_C0F(): pass

    label('loc_C0F')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_C29(): pass

    label('loc_C29')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0009 offset: 0xC3B
@scena.Code('func_09_C3B')
def func_09_C3B():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 5, 0x1E15)),
            Expr.Return,
        ),
        'loc_C43',
    )

    Return()

    def _loc_C43(): pass

    label('loc_C43')

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
        'loc_C68',
    )

    Call(0, 0x000F)
    Call(0, 0x0010)
    FadeIn(0, 0)
    Sleep(100)

    def _loc_C68(): pass

    label('loc_C68')

    Fade(1000)
    CameraMove(170, 400, 34390, 0)
    OP_67(0, 5030, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(359, 0)
    ChrSetPos(0x0101, 600, 400, 31000, 0)
    ChrSetPos(0x0102, -300, 400, 31000, 0)
    ChrSetPos(0x0103, 1000, 400, 29300, 0)
    ChrSetPos(0x00F9, -700, 400, 29300, 0)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C2, 4, 0x1E14)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10DF',
    )

    SetScenaFlags(ScenaFlag(0x03C2, 4, 0x1E14))
    PlaySE(280, 0x00, 0x64)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    OP_62(0x0103, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D75',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_DB3')

    def _loc_D75(): pass

    label('loc_D75')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D9C',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_DB3')

    def _loc_D9C(): pass

    label('loc_D9C')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_DB3(): pass

    label('loc_DB3')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010291381V#1004F#6P哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020341308V#1042F#6P刚才那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030341309V#024F#6P……退下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 0, 2500, 36580, 180)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 10)
    CreateThread(0x0008, 0x00, 0x00, func_02_598)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_0E6A')
    def lambda_0E6A():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0E6A)

    @scena.Lambda('lambda_0E7C')
    def lambda_0E7C():
        ChrMoveTo(0x00FE, 0, 700, 36580, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0E7C)

    @scena.Lambda('lambda_0E97')
    def lambda_0E97():
        CameraSetDistance(3000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E97)

    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, func_0D_141A)
    Sleep(50)

    CreateThread(0x0103, 0x00, 0x00, func_0C_13F3)
    Sleep(100)

    CreateThread(0x0102, 0x00, 0x00, func_0B_13CC)
    Sleep(100)

    CreateThread(0x0101, 0x00, 0x00, func_0A_13A5)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_0EF0')
    def lambda_0EF0():
        CameraMove(170, 400, 31000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0EF0)

    @scena.Lambda('lambda_0F08')
    def lambda_0F08():
        CameraSetDistance(2200, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0F08)

    ChrSetChipByIndex(0x0008, 11)

    @scena.Lambda('lambda_0F1D')
    def lambda_0F1D():
        ChrMoveTo(0x00FE, 150, 500, 30870, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0F1D)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0008, 0xFF)
    Battle(0x00000409, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_F5C'),
        (0x00000002, 'loc_101D'),
        (0x00000001, 'loc_10D7'),
        (-1, 'loc_10DC'),
    )

    def _loc_F5C(): pass

    label('loc_F5C')

    EventBegin(0x00)
    TerminateThread(0x0008, 0x02)
    ChrSetFlags(0x0008, 0x0080)
    CameraMove(460, 400, 30560, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 460, 400, 30560, 0)
    ChrSetPos(0x0001, 460, 400, 30560, 0)
    ChrSetPos(0x0002, 460, 400, 30560, 0)
    ChrSetPos(0x0003, 460, 400, 30560, 0)
    OP_69(0x0000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0103, 0)
    ChrSetSubChip(0x00F9, 0)
    SetScenaFlags(ScenaFlag(0x03C2, 5, 0x1E15))

    Jump('loc_10DC')

    def _loc_101D(): pass

    label('loc_101D')

    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    CameraMove(-30, 400, 25940, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 0, 400, 25940, 0)
    ChrSetPos(0x0001, 0, 400, 25940, 0)
    ChrSetPos(0x0002, 0, 400, 25940, 0)
    ChrSetPos(0x0003, 0, 400, 25940, 0)
    OP_69(0x0000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0103, 0)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_10DC')

    def _loc_10D7(): pass

    label('loc_10D7')

    OP_B4(0x00)

    Jump('loc_10DC')

    def _loc_10DC(): pass

    label('loc_10DC')

    Jump('loc_13A1')

    def _loc_10DF(): pass

    label('loc_10DF')

    PlaySE(280, 0x00, 0x64)
    Sleep(1000)

    ChrSetFlags(0x0008, 0x0004)
    ChrSetPos(0x0008, 0, 2500, 36580, 180)
    ChrSetRGBAMask(0x0008, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetChipByIndex(0x0008, 10)
    CreateThread(0x0008, 0x00, 0x00, func_02_598)

    ExecExpressionWithVar(
        0x1C,
        (
            (Expr.PushLong, 0x1),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(153, 0x00, 0x64)

    @scena.Lambda('lambda_112F')
    def lambda_112F():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_112F)

    @scena.Lambda('lambda_1141')
    def lambda_1141():
        ChrMoveTo(0x00FE, 0, 700, 36580, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1141)

    @scena.Lambda('lambda_115C')
    def lambda_115C():
        CameraSetDistance(3000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_115C)

    Sleep(300)

    CreateThread(0x00F9, 0x00, 0x00, func_0D_141A)
    Sleep(50)

    CreateThread(0x0103, 0x00, 0x00, func_0C_13F3)
    Sleep(100)

    CreateThread(0x0102, 0x00, 0x00, func_0B_13CC)
    Sleep(100)

    CreateThread(0x0101, 0x00, 0x00, func_0A_13A5)
    WaitForThreadExit(0x0008, 0x0001)
    WaitForThreadExit(0x0008, 0x0002)
    WaitForThreadExit(0x0101, 0x0000)
    WaitForThreadExit(0x0101, 0x0001)
    Sleep(500)

    @scena.Lambda('lambda_11B5')
    def lambda_11B5():
        CameraMove(170, 400, 31000, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_11B5)

    @scena.Lambda('lambda_11CD')
    def lambda_11CD():
        CameraSetDistance(2200, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11CD)

    ChrSetChipByIndex(0x0008, 11)

    @scena.Lambda('lambda_11E2')
    def lambda_11E2():
        ChrMoveTo(0x00FE, 150, 500, 30870, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_11E2)

    WaitForThreadExit(0x0101, 0x0000)
    TerminateThread(0x0008, 0xFF)
    Battle(0x00000409, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_1221'),
        (0x00000002, 'loc_12E2'),
        (0x00000001, 'loc_139C'),
        (-1, 'loc_13A1'),
    )

    def _loc_1221(): pass

    label('loc_1221')

    EventBegin(0x00)
    TerminateThread(0x0008, 0x02)
    ChrSetFlags(0x0008, 0x0080)
    CameraMove(460, 400, 30560, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 460, 400, 30560, 0)
    ChrSetPos(0x0001, 460, 400, 30560, 0)
    ChrSetPos(0x0002, 460, 400, 30560, 0)
    ChrSetPos(0x0003, 460, 400, 30560, 0)
    OP_69(0x0000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0103, 0)
    ChrSetSubChip(0x00F9, 0)
    SetScenaFlags(ScenaFlag(0x03C2, 5, 0x1E15))

    Jump('loc_13A1')

    def _loc_12E2(): pass

    label('loc_12E2')

    EventBegin(0x00)
    ChrSetFlags(0x0008, 0x0080)
    CameraMove(-30, 400, 25940, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 0, 400, 25940, 0)
    ChrSetPos(0x0001, 0, 400, 25940, 0)
    ChrSetPos(0x0002, 0, 400, 25940, 0)
    ChrSetPos(0x0003, 0, 400, 25940, 0)
    OP_69(0x0000, 0)
    ChrSetChipByIndex(0x0101, 65535)
    ChrSetChipByIndex(0x0102, 65535)
    ChrSetChipByIndex(0x0103, 65535)
    ChrSetChipByIndex(0x00F9, 65535)
    ChrSetSubChip(0x0101, 0)
    ChrSetSubChip(0x0102, 0)
    ChrSetSubChip(0x0103, 0)
    ChrSetSubChip(0x00F9, 0)

    Jump('loc_13A1')

    def _loc_139C(): pass

    label('loc_139C')

    OP_B4(0x00)

    Jump('loc_13A1')

    def _loc_13A1(): pass

    label('loc_13A1')

    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x000A offset: 0x13A5
@scena.Code('func_0A_13A5')
def func_0A_13A5():
    ChrJumpTo(0x00FE, 600, 400, 29000, 400, 6000)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x00FE, 14)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x000B offset: 0x13CC
@scena.Code('func_0B_13CC')
def func_0B_13CC():
    ChrJumpTo(0x00FE, -300, 400, 29000, 400, 6000)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x00FE, 15)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x000C offset: 0x13F3
@scena.Code('func_0C_13F3')
def func_0C_13F3():
    ChrJumpTo(0x00FE, 1000, 400, 27300, 400, 6000)
    PlaySE(213, 0x00, 0x64)
    ChrSetChipByIndex(0x00FE, 16)
    ChrSetSubChip(0x00FE, 0)

    Return()

# id: 0x000D offset: 0x141A
@scena.Code('func_0D_141A')
def func_0D_141A():
    ChrJumpTo(0x00FE, -700, 400, 27300, 400, 6000)
    ChrSetSubChip(0x00FE, 0)

    Switch(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            Expr.Return,
        ),
        (0x00000005, 'loc_1453'),
        (0x00000004, 'loc_145B'),
        (0x00000006, 'loc_1463'),
        (0x00000007, 'loc_146B'),
        (0x00000008, 'loc_1473'),
        (-1, 'loc_147B'),
    )

    def _loc_1453(): pass

    label('loc_1453')

    ChrSetChipByIndex(0x00F9, 17)

    Jump('loc_147B')

    def _loc_145B(): pass

    label('loc_145B')

    ChrSetChipByIndex(0x00F9, 18)

    Jump('loc_147B')

    def _loc_1463(): pass

    label('loc_1463')

    ChrSetChipByIndex(0x00F9, 19)

    Jump('loc_147B')

    def _loc_146B(): pass

    label('loc_146B')

    ChrSetChipByIndex(0x00F9, 20)

    Jump('loc_147B')

    def _loc_1473(): pass

    label('loc_1473')

    ChrSetChipByIndex(0x00F9, 21)

    Jump('loc_147B')

    def _loc_147B(): pass

    label('loc_147B')

    Return()

# id: 0x000E offset: 0x147C
@scena.Code('func_0E_147C')
def func_0E_147C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x03C3, 3, 0x1E1B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1782',
    )

    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(156, 0x00, 0x64)
    OP_B0(0x0000, 0x78)
    OP_70(0x0000, 360)
    Sleep(2500)

    PlaySE(157, 0x00, 0x64)
    OP_B0(0x0004, 0x64)
    OP_B0(0x0005, 0x64)
    OP_B0(0x0006, 0x64)
    OP_B0(0x0007, 0x64)
    OP_70(0x0004, 240)
    Sleep(100)

    OP_70(0x0005, 240)
    Sleep(100)

    OP_70(0x0006, 240)
    Sleep(100)

    OP_70(0x0007, 240)
    Sleep(100)

    PlaySE(185, 0x00, 0x64)
    OP_B0(0x0001, 0x64)
    OP_B0(0x0002, 0x64)
    OP_B0(0x0003, 0x64)
    OP_70(0x0001, 360)
    OP_70(0x0002, 360)
    OP_70(0x0003, 360)
    OP_73(0x0001)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S关于『环』的封印（１／４）\n',
            '　\n',
            '地■■■的建造■■完■■时候\n',
            '■知■■中\n',
            '『■■得知■『■■■■』\n',
            '　\n',
            '■因是■■同■禁不住『■』的诱■，\n',
            '精神被■介■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S不过■那个同胞\n',
            '并没有■■可以得知计划全貌■地■\n',
            '■■不幸■■■■\n',
            '　\n',
            '『■』■■■■长城■■■■■\n',
            '和『设■■■，\n',
            '只捉■■湖■的■■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['数据水晶８']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    AddItem(ItemTable['数据水晶８'], 1)
    SetScenaFlags(ScenaFlag(0x03C3, 3, 0x1E1B))
    Sleep(100)

    FadeOut(1000, 0, -1)
    OP_0D()
    OP_6F(0x0000, 360)
    OP_6F(0x0001, 0)
    OP_6F(0x0002, 0)
    OP_6F(0x0003, 0)
    OP_6F(0x0004, 0)
    OP_6F(0x0005, 0)
    OP_6F(0x0006, 0)
    OP_6F(0x0007, 0)
    CameraMove(350, 200, 36760, 0)
    OP_67(0, 7500, -10000, 0)
    CameraSetDistance(4000, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0000, 350, 200, 36760, 0)
    ChrSetPos(0x0001, 350, 200, 36760, 0)
    ChrSetPos(0x0002, 350, 200, 36760, 0)
    ChrSetPos(0x0003, 350, 200, 36760, 0)
    OP_69(0x0000, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)

    Jump('loc_18EC')

    def _loc_1782(): pass

    label('loc_1782')

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    PlaySE(156, 0x00, 0x64)
    Sleep(300)

    FadeOut(300, 0, 100)
    SetMessageWindowPos(330, 68, 34, 12)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S关于『环』的封印（１／４）\n',
            '　\n',
            '地■■■的建造■■完■■时候\n',
            '■知■■中\n',
            '『■■得知■『■■■■』\n',
            '　\n',
            '■因是■■同■禁不住『■』的诱■，\n',
            '精神被■介■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#1S不过■那个同胞\n',
            '并没有■■可以得知计划全貌■地■\n',
            '■■不幸■■■■\n',
            '　\n',
            '『■』■■■■长城■■■■■\n',
            '和『设■■■，\n',
            '只捉■■湖■的■■■■。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_0D()

    def _loc_18EC(): pass

    label('loc_18EC')

    TalkEnd(0x00FF)

    Return()

# id: 0x000F offset: 0x18F0
@scena.Code('func_0F_18F0')
def func_0F_18F0():
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
        (0x00000000, 'loc_196A'),
        (0x00000001, 'loc_1970'),
        (-1, 'loc_1976'),
    )

    def _loc_196A(): pass

    label('loc_196A')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1976')

    def _loc_1970(): pass

    label('loc_1970')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1976')

    def _loc_1976(): pass

    label('loc_1976')

    Return()

# id: 0x0010 offset: 0x1977
@scena.Code('func_10_1977')
def func_10_1977():
    FadeOut(0, 0, -1)
    CameraMove(-48940, 490, -13310, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
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

# id: 0x0011 offset: 0x1A04
@scena.Code('func_11_1A04')
def func_11_1A04():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 200, -66500, 0)
    OP_6C(225000, 0)
    ChrSetPos(0x0101, -500, 200, -66000, 0)
    ChrSetPos(0x0102, 500, 200, -66000, 0)
    ChrSetPos(0x00F8, -500, 200, -67000, 0)
    ChrSetPos(0x00F9, 500, 200, -67000, 0)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0015)
    Call(0, 0x0017)
    Fade(500)
    CameraMove(-70, 200, -64510, 0)
    OP_6C(315000, 0)
    ChrSetPos(0x0000, -70, 200, -64510, 0)
    ChrSetPos(0x0001, -70, 200, -64510, 0)
    ChrSetPos(0x0002, -70, 200, -64510, 0)
    ChrSetPos(0x0003, -70, 200, -64510, 0)
    EventEnd(0x00)

    Return()

# id: 0x0012 offset: 0x1B11
@scena.Code('func_12_1B11')
def func_12_1B11():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(0, 200, -66500, 0)
    OP_6C(225000, 0)
    ChrSetPos(0x0101, 500, 200, -67000, 180)
    ChrSetPos(0x0102, -500, 200, -67000, 180)
    ChrSetPos(0x00F8, 500, 200, -66000, 180)
    ChrSetPos(0x00F9, -500, 200, -66000, 180)
    OP_0D()
    Call(0, 0x0015)
    Call(0, 0x0018)
    NewScene('ED6_DT21/C2300._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0013 offset: 0x1B92
@scena.Code('func_13_1B92')
def func_13_1B92():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    CameraMove(0, 200, 66500, 0)
    ChrSetPos(0x0101, 500, 200, 66000, 180)
    ChrSetPos(0x0102, -500, 200, 66000, 180)
    ChrSetPos(0x00F8, 500, 200, 67000, 180)
    ChrSetPos(0x00F9, -500, 200, 67000, 180)
    ChrSetRGBAMask(0x0000, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0001, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0002, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0003, 255, 255, 255, 0, 0)
    FadeIn(500, 0)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0017)
    Fade(500)
    CameraMove(80, 200, 64560, 0)
    ChrSetPos(0x0000, 80, 200, 64560, 180)
    ChrSetPos(0x0001, 80, 200, 64560, 180)
    ChrSetPos(0x0002, 80, 200, 64560, 180)
    ChrSetPos(0x0003, 80, 200, 64560, 180)
    EventEnd(0x00)

    Return()

# id: 0x0014 offset: 0x1C8D
@scena.Code('func_14_1C8D')
def func_14_1C8D():
    EventBegin(0x01)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Fade(500)
    CameraMove(0, 200, 66500, 0)
    ChrSetPos(0x0101, -500, 200, 67000, 0)
    ChrSetPos(0x0102, 500, 200, 67000, 0)
    ChrSetPos(0x00F8, -500, 200, 66000, 0)
    ChrSetPos(0x00F9, 500, 200, 66000, 0)
    OP_0D()
    Call(0, 0x0016)
    Call(0, 0x0018)
    NewScene('ED6_DT21/C2302._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0015 offset: 0x1D05
@scena.Code('func_15_1D05')
def func_15_1D05():
    PlayEffect(0x00, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x0016 offset: 0x1DE4
@scena.Code('func_16_1DE4')
def func_16_1DE4():
    PlayEffect(0x01, 0xFF, 0x0000, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0001, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0002, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x01, 0xFF, 0x0003, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(153, 0x00, 0x64)
    PlaySE(184, 0x00, 0x64)

    Return()

# id: 0x0017 offset: 0x1EC3
@scena.Code('func_17_1EC3')
def func_17_1EC3():
    @scena.Lambda('lambda_1EC9')
    def lambda_1EC9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1EC9)

    @scena.Lambda('lambda_1EDB')
    def lambda_1EDB():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1EDB)

    @scena.Lambda('lambda_1EED')
    def lambda_1EED():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1EED)

    @scena.Lambda('lambda_1EFF')
    def lambda_1EFF():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1EFF)

    Sleep(2500)

    Return()

# id: 0x0018 offset: 0x1F11
@scena.Code('func_18_1F11')
def func_18_1F11():
    @scena.Lambda('lambda_1F17')
    def lambda_1F17():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1F17)

    @scena.Lambda('lambda_1F29')
    def lambda_1F29():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1F29)

    @scena.Lambda('lambda_1F3B')
    def lambda_1F3B():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1F3B)

    @scena.Lambda('lambda_1F4D')
    def lambda_1F4D():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1F4D)

    Sleep(2000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
