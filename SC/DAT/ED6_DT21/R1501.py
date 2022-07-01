import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1501_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1501   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '拉文努村方向'),
    TXT(0x02, '拉文努废坑方向'),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1501.x'
    header.mapIndex       = 59
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7ED
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
        ('ED6_DT09/CH10030._CH', 'ED6_DT09/CH10030P._CP'),
        ('ED6_DT09/CH10031._CH', 'ED6_DT09/CH10031P._CP'),
        ('ED6_DT09/CH10860._CH', 'ED6_DT09/CH10860P._CP'),
        ('ED6_DT09/CH10861._CH', 'ED6_DT09/CH10861P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10330._CH', 'ED6_DT09/CH10330P._CP'),
        ('ED6_DT09/CH10331._CH', 'ED6_DT09/CH10331P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 36890,
            z                   = 30,
            y                   = -87580,
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
            x                   = -7320,
            z                   = -50,
            y                   = -39290,
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

# id: 0x10003 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 49340,
            z           = -40,
            y           = -22100,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 65019,
            z           = 0,
            y           = -52280,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0130,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 86970,
            z           = 40,
            y           = -28980,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 37970,
            z           = 40,
            y           = 3380,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0130,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 36750,
            z           = 10,
            y           = 20760,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 24510,
            z           = -50,
            y           = -10220,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x012F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1D2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 89310,
            triggerZ            = -90,
            triggerY            = -37830,
            triggerRange        = 1000,
            actorX              = 89340,
            actorZ              = 1400,
            actorY              = -37210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22370,
            triggerZ            = -20,
            triggerY            = 13370,
            triggerRange        = 1000,
            actorX              = 22100,
            actorZ              = 1480,
            actorY              = 13030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 99270,
            triggerZ            = -50,
            triggerY            = -16890,
            triggerRange        = 1000,
            actorX              = 99270,
            actorZ              = 1450,
            actorY              = -16890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 17400,
            triggerZ            = 50,
            triggerY            = -11850,
            triggerRange        = 1000,
            actorX              = 16740,
            actorZ              = 130,
            actorY              = -11850,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 54310,
            triggerZ            = -130,
            triggerY            = 8750,
            triggerRange        = 1000,
            actorX              = 55060,
            actorZ              = -130,
            actorY              = 8750,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 37000,
            triggerZ            = 0,
            triggerY            = -41450,
            triggerRange        = 1500,
            actorX              = 37000,
            actorZ              = 150,
            actorY              = -41450,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2AA
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x2AB
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFEDB08, 0xFFFDAE40, 0x00230020)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 2, 0x1A1A)),
            (Expr.TestScenaFlags, ScenaFlag(0x0343, 4, 0x1A1C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D5',
    )

    OP_B1('R1501_y')

    Jump('loc_2DE')

    def _loc_2D5(): pass

    label('loc_2D5')

    OP_B1('R1501_n')

    def _loc_2DE(): pass

    label('loc_2DE')

    ClearMapFlags(0x02000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 2, 0x1B22)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2F5',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2FC')

    def _loc_2F5(): pass

    label('loc_2F5')

    OP_6F(0x0000, 60)

    def _loc_2FC(): pass

    label('loc_2FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 3, 0x1B23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_30E',
    )

    OP_6F(0x0001, 0)

    Jump('loc_315')

    def _loc_30E(): pass

    label('loc_30E')

    OP_6F(0x0001, 60)

    def _loc_315(): pass

    label('loc_315')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 4, 0x1B24)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_327',
    )

    OP_6F(0x0002, 0)

    Jump('loc_32E')

    def _loc_327(): pass

    label('loc_327')

    OP_6F(0x0002, 60)

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 6, 0x1B26)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_340',
    )

    OP_6F(0x0003, 0)

    Jump('loc_347')

    def _loc_340(): pass

    label('loc_340')

    OP_6F(0x0003, 60)

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 7, 0x1B27)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_359',
    )

    OP_6F(0x0004, 0)

    Jump('loc_360')

    def _loc_359(): pass

    label('loc_359')

    OP_6F(0x0004, 60)

    def _loc_360(): pass

    label('loc_360')

    OP_64(0x03, 0x0001)
    OP_71(0x0003, 0x0000)
    OP_71(0x0003, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0344, 4, 0x1A24)),
            Expr.Return,
        ),
        'loc_381',
    )

    OP_10(0x00, 0x00)
    OP_10(0x02, 0x00)
    OP_10(0x03, 0x01)

    Jump('loc_38E')

    def _loc_381(): pass

    label('loc_381')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0342, 3, 0x1A13)),
            Expr.Return,
        ),
        'loc_38E',
    )

    OP_10(0x00, 0x00)
    OP_10(0x02, 0x01)

    def _loc_38E(): pass

    label('loc_38E')

    Return()

# id: 0x0002 offset: 0x38F
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xD9, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 2, 0x1B22)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_46C',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['白虎之爪'], 1)"),
            Expr.Return,
        ),
        'loc_403',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['白虎之爪']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B22)

    Jump('loc_469')

    def _loc_403(): pass

    label('loc_403')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['白虎之爪']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['白虎之爪']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_469(): pass

    label('loc_469')

    Jump('loc_49D')

    def _loc_46C(): pass

    label('loc_46C')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_49D(): pass

    label('loc_49D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x4AB
@scena.Code('func_03_4AB')
def func_03_4AB():
    UnlockAchievement(0x02, 0xDA, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 3, 0x1B23)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_588',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_51F',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B23)

    Jump('loc_585')

    def _loc_51F(): pass

    label('loc_51F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['中回复药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_585(): pass

    label('loc_585')

    Jump('loc_5B9')

    def _loc_588(): pass

    label('loc_588')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_5B9(): pass

    label('loc_5B9')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5C7
@scena.Code('func_04_5C7')
def func_04_5C7():
    UnlockAchievement(0x02, 0xDB, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 4, 0x1B24)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_645',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000001E)
    OP_73(0x0002)
    OP_6F(0x0002, 30)
    AddSepith(0x02, 0x00C8)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×２００\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B24)

    Jump('loc_65F')

    def _loc_645(): pass

    label('loc_645')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_65F(): pass

    label('loc_65F')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x671
@scena.Code('func_05_671')
def func_05_671():
    Return()

# id: 0x0006 offset: 0x672
@scena.Code('func_06_672')
def func_06_672():
    UnlockAchievement(0x02, 0xDC, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0364, 7, 0x1B27)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_74F',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_6E6',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B27)

    Jump('loc_74C')

    def _loc_6E6(): pass

    label('loc_6E6')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['复苏药']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)

    def _loc_74C(): pass

    label('loc_74C')

    Jump('loc_780')

    def _loc_74F(): pass

    label('loc_74F')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    def _loc_780(): pass

    label('loc_780')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0007 offset: 0x78E
@scena.Code('func_07_78E')
def func_07_78E():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　拉文努矿山　１４０塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
