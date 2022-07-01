import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C4100_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4100   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '庭园大道方向'),
    TXT(0x02, '艾尔贝离宫方向'),
    TXT(0x03, '罗马尔池方向'),
    TXT(0x04, '鬼草'),
    TXT(0x05, '鳄鱼'),
    TXT(0x06, '凶暴巨鳄'),
    TXT(0x07, '蝙蝠'),
    TXT(0x08, '迅猛小鹫'),
    TXT(0x09, '地狱火爆麻雀'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4100.x'
    header.mapIndex       = 1
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5FD
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
        ('ED6_DT09/CH10780._CH', 'ED6_DT09/CH10780P._CP'),
        ('ED6_DT09/CH10781._CH', 'ED6_DT09/CH10781P._CP'),
        ('ED6_DT09/CH10790._CH', 'ED6_DT09/CH10790P._CP'),
        ('ED6_DT09/CH10791._CH', 'ED6_DT09/CH10791P._CP'),
        ('ED6_DT09/CH10050._CH', 'ED6_DT09/CH10050P._CP'),
        ('ED6_DT09/CH10051._CH', 'ED6_DT09/CH10051P._CP'),
        ('ED6_DT09/CH10800._CH', 'ED6_DT09/CH10800P._CP'),
        ('ED6_DT09/CH10801._CH', 'ED6_DT09/CH10801P._CP'),
        ('ED6_DT09/CH10810._CH', 'ED6_DT09/CH10810P._CP'),
        ('ED6_DT09/CH10811._CH', 'ED6_DT09/CH10811P._CP'),
        ('ED6_DT09/CH10820._CH', 'ED6_DT09/CH10820P._CP'),
        ('ED6_DT09/CH10821._CH', 'ED6_DT09/CH10821P._CP'),
        ('ED6_DT09/CH11220._CH', 'ED6_DT09/CH11220P._CP'),
        ('ED6_DT09/CH11221._CH', 'ED6_DT09/CH11221P._CP'),
        ('ED6_DT09/CH11230._CH', 'ED6_DT09/CH11230P._CP'),
        ('ED6_DT09/CH11231._CH', 'ED6_DT09/CH11231P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 980,
            z                   = 0,
            y                   = 71400,
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
            x                   = -43080,
            z                   = 0,
            y                   = -63930,
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
            x                   = 27730,
            z                   = 0,
            y                   = -2770,
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

# id: 0x10003 offset: 0x18A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 11100,
            z           = -20,
            y           = 24620,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6780,
            z           = 40,
            y           = 21320,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025D,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -2830,
            z           = 0,
            y           = -29020,
            word_0C     = 0x0000,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -50760,
            z           = 0,
            y           = 12800,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -44310,
            z           = 30,
            y           = -2880,
            word_0C     = 0x0000,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0260,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -34560,
            z           = 170,
            y           = 8670,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x025F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -34880,
            triggerZ            = 80,
            triggerY            = 3840,
            triggerRange        = 1000,
            actorX              = -34320,
            actorZ              = 1590,
            actorY              = 3790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -11000,
            triggerZ            = 0,
            triggerY            = -39890,
            triggerRange        = 1000,
            actorX              = -11070,
            actorZ              = 0,
            actorY              = -40530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -44400,
            triggerZ            = 500,
            triggerY            = 7650,
            triggerRange        = 1500,
            actorX              = -44400,
            actorZ              = 4000,
            actorY              = 7650,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x29E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CC',
    )

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)

    def _loc_2CC(): pass

    label('loc_2CC')

    Return()

# id: 0x0001 offset: 0x2CD
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFDE4F0, 0xFFFE0C00, 0x00230063)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 5, 0x1625)),
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_309',
    )

    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    SetChrFlags(0x0010, 0x0080)

    def _loc_309(): pass

    label('loc_309')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 0, 0x1700)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31B',
    )

    OP_6F(0x0003, 0)

    Jump('loc_322')

    def _loc_31B(): pass

    label('loc_31B')

    OP_6F(0x0003, 60)

    def _loc_322(): pass

    label('loc_322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 2, 0x1702)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_334',
    )

    OP_6F(0x0004, 0)

    Jump('loc_33B')

    def _loc_334(): pass

    label('loc_334')

    OP_6F(0x0004, 60)

    def _loc_33B(): pass

    label('loc_33B')

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)

    Return()

# id: 0x0002 offset: 0x34B
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xF8, 0x00, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 0, 0x1700)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_469',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000001E)
    OP_73(0x0003)
    OP_6F(0x0003, 30)
    AddSepith(0x00, 0x0014)
    AddSepith(0x01, 0x0014)
    AddSepith(0x02, 0x0014)
    AddSepith(0x03, 0x0014)
    AddSepith(0x04, 0x0014)
    AddSepith(0x05, 0x0014)
    AddSepith(0x06, 0x0014)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#56I地之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#57I水之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#58I火之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#59I风之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×２０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1700)

    Jump('loc_483')

    def _loc_469(): pass

    label('loc_469')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_483(): pass

    label('loc_483')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x495
@scena.Code('func_03_495')
def func_03_495():
    UnlockAchievement(0x02, 0xF9, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02E0, 2, 0x1702)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_572',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_509',
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
    OP_A2(0x1702)

    Jump('loc_56F')

    def _loc_509(): pass

    label('loc_509')

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
    OP_6F(0x0004, 60)
    OP_70(0x0004, 0x00000000)

    def _loc_56F(): pass

    label('loc_56F')

    Jump('loc_5A3')

    def _loc_572(): pass

    label('loc_572')

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
    def _loc_5A3(): pass

    label('loc_5A3')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5B1
@scena.Code('func_04_5B1')
def func_04_5B1():
    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '有一块陈旧的翠耀石石碑。',
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
