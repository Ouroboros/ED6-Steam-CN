import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C1215_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C1215   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'C1215.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x7C5
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
        ('ED6_DT09/CH10410._CH', 'ED6_DT09/CH10410P._CP'),
        ('ED6_DT09/CH10411._CH', 'ED6_DT09/CH10411P._CP'),
        ('ED6_DT09/CH10420._CH', 'ED6_DT09/CH10420P._CP'),
        ('ED6_DT09/CH10421._CH', 'ED6_DT09/CH10421P._CP'),
        ('ED6_DT09/CH10430._CH', 'ED6_DT09/CH10430P._CP'),
        ('ED6_DT09/CH10431._CH', 'ED6_DT09/CH10431P._CP'),
        ('ED6_DT09/CH10440._CH', 'ED6_DT09/CH10440P._CP'),
        ('ED6_DT09/CH10441._CH', 'ED6_DT09/CH10441P._CP'),
        ('ED6_DT29/CH12500._CH', 'ED6_DT29/CH12500P._CP'),
    ]

# id: 0x10002 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -8890,
            z                   = 1000,
            y                   = 8860,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -60,
            z                   = 0,
            y                   = -18410,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x132
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -30,
            z           = 0,
            y           = 17960,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x008F,
            word_18     = 0x1BAB,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -60,
            z           = 0,
            y           = -6100,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x008F,
            word_18     = 0x1BAC,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x16A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x16A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 11840,
            triggerZ            = 0,
            triggerY            = 40,
            triggerRange        = 1000,
            actorX              = 12620,
            actorZ              = 0,
            actorY              = 60,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -11810,
            triggerZ            = 0,
            triggerY            = -40,
            triggerRange        = 1000,
            actorX              = -12660,
            actorZ              = 0,
            actorY              = 90,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -8390,
            triggerZ            = 0,
            triggerY            = 8360,
            triggerRange        = 1000,
            actorX              = -8890,
            actorZ              = 0,
            actorY              = 8860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 8290,
            triggerZ            = 0,
            triggerY            = 8360,
            triggerRange        = 1000,
            actorX              = 8750,
            actorZ              = 0,
            actorY              = 8820,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1FA
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1FB
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 7, 0x1B67)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20D',
    )

    OP_6F(0x0000, 0)

    Jump('loc_214')

    def _loc_20D(): pass

    label('loc_20D')

    OP_6F(0x0000, 60)

    def _loc_214(): pass

    label('loc_214')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036D, 1, 0x1B69)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_226',
    )

    OP_6F(0x0001, 0)

    Jump('loc_22D')

    def _loc_226(): pass

    label('loc_226')

    OP_6F(0x0001, 60)

    def _loc_22D(): pass

    label('loc_22D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036D, 3, 0x1B6B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_23F',
    )

    OP_6F(0x0002, 0)

    Jump('loc_246')

    def _loc_23F(): pass

    label('loc_23F')

    OP_6F(0x0002, 60)

    def _loc_246(): pass

    label('loc_246')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036D, 5, 0x1B6D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_258',
    )

    OP_6F(0x0003, 0)

    Jump('loc_25F')

    def _loc_258(): pass

    label('loc_258')

    OP_6F(0x0003, 60)

    def _loc_25F(): pass

    label('loc_25F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0375, 3, 0x1BAB)),
            Expr.Return,
        ),
        'loc_26B',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_26B(): pass

    label('loc_26B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0375, 4, 0x1BAC)),
            Expr.Return,
        ),
        'loc_277',
    )

    SetChrFlags(0x000B, 0x0080)

    def _loc_277(): pass

    label('loc_277')

    Return()

# id: 0x0002 offset: 0x278
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_28D',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_28D(): pass

    label('loc_28D')

    Return()

# id: 0x0003 offset: 0x28E
@scena.Code('func_03_28E')
def func_03_28E():
    UnlockAchievement(0x02, 0x43, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036C, 7, 0x1B67)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_36B',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['兔跃靴'], 1)"),
            Expr.Return,
        ),
        'loc_302',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['兔跃靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B67)

    Jump('loc_368')

    def _loc_302(): pass

    label('loc_302')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['兔跃靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['兔跃靴']),
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

    def _loc_368(): pass

    label('loc_368')

    Jump('loc_39C')

    def _loc_36B(): pass

    label('loc_36B')

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
    def _loc_39C(): pass

    label('loc_39C')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x3AA
@scena.Code('func_04_3AA')
def func_04_3AA():
    UnlockAchievement(0x02, 0x44, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036D, 1, 0x1B69)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_487',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['长桶Ⅱ'], 1)"),
            Expr.Return,
        ),
        'loc_41E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['长桶Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B69)

    Jump('loc_484')

    def _loc_41E(): pass

    label('loc_41E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['长桶Ⅱ']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['长桶Ⅱ']),
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

    def _loc_484(): pass

    label('loc_484')

    Jump('loc_4B8')

    def _loc_487(): pass

    label('loc_487')

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
    def _loc_4B8(): pass

    label('loc_4B8')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x4C6
@scena.Code('func_05_4C6')
def func_05_4C6():
    UnlockAchievement(0x02, 0x45, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036D, 3, 0x1B6B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_65E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036D, 4, 0x1B6C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5AA',
    )

    OP_9F(0x0008, 0xFF, 0xFF, 0xFF, 0x00, 0x00000000)
    ChrTurnDirection(0x0008, 0x0000, 0)
    OP_91(0x0008, 0, 1000, 0, 0, 0x00)

    @scena.Lambda('lambda_051D')
    def lambda_051D():
        OP_91(0x00FE, 0, -1000, 0, 600, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_051D)

    @scena.Lambda('lambda_0538')
    def lambda_0538():
        OP_9F(0x00FE, 0xFF, 0xFF, 0xFF, 0xFF, 0x00000258)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_0538)

    ClearChrFlags(0x0008, 0x0080)

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
    Battle(0x00000092, 0x00000000, 0x00, 0x0000, 0xFF)
    SetChrFlags(0x0008, 0x0080)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000000, 'loc_585'),
        (0x00000002, 'loc_597'),
        (0x00000001, 'loc_5A7'),
        (-1, 'loc_5AA'),
    )

    def _loc_585(): pass

    label('loc_585')

    OP_A2(0x1B6C)
    OP_6F(0x0002, 60)
    Sleep(500)

    Jump('loc_5AA')

    def _loc_597(): pass

    label('loc_597')

    OP_6F(0x0002, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

    def _loc_5A7(): pass

    label('loc_5A7')

    OP_B4(0x00)

    Return()

    def _loc_5AA(): pass

    label('loc_5AA')

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['导力靴'], 1)"),
            Expr.Return,
        ),
        'loc_5F9',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['导力靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B6B)

    Jump('loc_65B')

    def _loc_5F9(): pass

    label('loc_5F9')

    FadeOut(300, 0, 100)

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['导力靴']),
            (TxtCtl.SetColor, 0x0),
            '。 \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['导力靴']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0x00000000)

    def _loc_65B(): pass

    label('loc_65B')

    Jump('loc_68D')

    def _loc_65E(): pass

    label('loc_65E')

    FadeOut(300, 0, 100)

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
    def _loc_68D(): pass

    label('loc_68D')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x69B
@scena.Code('func_06_69B')
def func_06_69B():
    UnlockAchievement(0x02, 0x46, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x036D, 5, 0x1B6D)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_778',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0003, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['替身木偶'], 1)"),
            Expr.Return,
        ),
        'loc_70F',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B6D)

    Jump('loc_775')

    def _loc_70F(): pass

    label('loc_70F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['替身木偶']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0003, 60)
    OP_70(0x0003, 0x00000000)

    def _loc_775(): pass

    label('loc_775')

    Jump('loc_7A9')

    def _loc_778(): pass

    label('loc_778')

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
    def _loc_7A9(): pass

    label('loc_7A9')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
