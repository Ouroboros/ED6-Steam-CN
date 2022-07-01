import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
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
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0301.x'
    header.mapIndex       = 19
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6AF
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000088B8,
            dword_04        = 0x00000000,
            dword_08        = 0x00003E80,
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
            word_3A         = 19,
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
        ('ED6_DT29/CH12430._CH', 'ED6_DT29/CH12430P._CP'),
        ('ED6_DT29/CH12431._CH', 'ED6_DT29/CH12431P._CP'),
        ('ED6_DT09/CH10010._CH', 'ED6_DT09/CH10010P._CP'),
        ('ED6_DT09/CH10011._CH', 'ED6_DT09/CH10011P._CP'),
        ('ED6_DT09/CH10280._CH', 'ED6_DT09/CH10280P._CP'),
        ('ED6_DT09/CH10281._CH', 'ED6_DT09/CH10281P._CP'),
        ('ED6_DT29/CH12400._CH', 'ED6_DT29/CH12400P._CP'),
        ('ED6_DT29/CH12401._CH', 'ED6_DT29/CH12401P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xEA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 6930,
            z           = 40,
            y           = -26770,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5350,
            z           = -180,
            y           = -27890,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -15690,
            z           = -310,
            y           = 1410,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -3030,
            z           = 410,
            y           = 24850,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 6930,
            z           = 40,
            y           = -26770,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0040,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -5350,
            z           = -180,
            y           = -27890,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0041,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -15690,
            z           = -310,
            y           = 1410,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0042,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -3030,
            z           = 410,
            y           = 24850,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0041,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1CA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1CA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -14410,
            triggerZ            = -120,
            triggerY            = 8350,
            triggerRange        = 1000,
            actorX              = -14410,
            actorZ              = -120,
            actorY              = 9060,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -22500,
            triggerZ            = -150,
            triggerY            = 35130,
            triggerRange        = 1000,
            actorX              = -22500,
            actorZ              = -150,
            actorY              = 35720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 18070,
            triggerZ            = -120,
            triggerY            = 17440,
            triggerRange        = 1000,
            actorX              = 18470,
            actorZ              = -120,
            actorY              = 17840,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x236
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x237
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 3, 0x1823)),
            (Expr.TestScenaFlags, ScenaFlag(0x0316, 0, 0x18B0)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_246',
    )

    OP_64(0x03, 0x0001)

    def _loc_246(): pass

    label('loc_246')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 1, 0x1961)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_258',
    )

    OP_6F(0x0004, 0)

    Jump('loc_25F')

    def _loc_258(): pass

    label('loc_258')

    OP_6F(0x0004, 60)

    def _loc_25F(): pass

    label('loc_25F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 2, 0x1962)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_271',
    )

    OP_6F(0x0005, 0)

    Jump('loc_278')

    def _loc_271(): pass

    label('loc_271')

    OP_6F(0x0005, 60)

    def _loc_278(): pass

    label('loc_278')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 4, 0x1964)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_28A',
    )

    OP_6F(0x0006, 0)

    Jump('loc_291')

    def _loc_28A(): pass

    label('loc_28A')

    OP_6F(0x0006, 60)

    def _loc_291(): pass

    label('loc_291')

    ExecExpressionWithValue(
        0x000C,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000E,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000F,
        0x24,
        (
            (Expr.PushLong, 0xDF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_71(0x0002, 0x0004)
    OP_71(0x0003, 0x0004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_2EF',
    )

    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    SetChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000B, 0x0080)

    Jump('loc_303')

    def _loc_2EF(): pass

    label('loc_2EF')

    SetChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)

    def _loc_303(): pass

    label('loc_303')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_331',
    )

    OP_C4(0x00, 0x00000004)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_331',
    )

    SetMapFlags(0x00000010)
    OP_11(0xE6, 0xF0, 0xFF, 0x00000000, 0x0000EA60, 0x00000000)

    def _loc_331(): pass

    label('loc_331')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 4, 0x1824)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34A',
    )

    OP_10(0x02, 0x00)
    OP_10(0x04, 0x01)

    Jump('loc_350')

    def _loc_34A(): pass

    label('loc_34A')

    OP_10(0x02, 0x01)
    OP_10(0x04, 0x00)

    def _loc_350(): pass

    label('loc_350')

    Return()

# id: 0x0002 offset: 0x351
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x02, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 1, 0x1961)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_42E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0004, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['狼牙鞭'], 1)"),
            Expr.Return,
        ),
        'loc_3C5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['狼牙鞭']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1961)

    Jump('loc_42B')

    def _loc_3C5(): pass

    label('loc_3C5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['狼牙鞭']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['狼牙鞭']),
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

    def _loc_42B(): pass

    label('loc_42B')

    Jump('loc_45F')

    def _loc_42E(): pass

    label('loc_42E')

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
    def _loc_45F(): pass

    label('loc_45F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x46D
@scena.Code('func_03_46D')
def func_03_46D():
    UnlockAchievement(0x02, 0x03, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 2, 0x1962)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_54A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0005, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['岩钉靴子'], 1)"),
            Expr.Return,
        ),
        'loc_4E1',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['岩钉靴子']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1962)

    Jump('loc_547')

    def _loc_4E1(): pass

    label('loc_4E1')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['岩钉靴子']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['岩钉靴子']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0005, 60)
    OP_70(0x0005, 0x00000000)

    def _loc_547(): pass

    label('loc_547')

    Jump('loc_57B')

    def _loc_54A(): pass

    label('loc_54A')

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
    def _loc_57B(): pass

    label('loc_57B')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x589
@scena.Code('func_04_589')
def func_04_589():
    UnlockAchievement(0x02, 0x04, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032C, 4, 0x1964)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_666',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0006, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['圣灵药'], 1)"),
            Expr.Return,
        ),
        'loc_5FD',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

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
    OP_A2(0x1964)

    Jump('loc_663')

    def _loc_5FD(): pass

    label('loc_5FD')

    FadeOut(300, 0, 100)
    SetChrName('')

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
    OP_22(0x002C, 0x00, 0x64)
    OP_6F(0x0006, 60)
    OP_70(0x0006, 0x00000000)

    def _loc_663(): pass

    label('loc_663')

    Jump('loc_697')

    def _loc_666(): pass

    label('loc_666')

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
    def _loc_697(): pass

    label('loc_697')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
