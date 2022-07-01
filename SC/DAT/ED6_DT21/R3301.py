import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R3301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R3301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '利塔街道方向'),
    TXT(0x02, '雷斯顿要塞方向'),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
    TXT(0x09, ''),
    TXT(0x0A, ''),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'R3301.x'
    header.mapIndex       = 1
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x6D6
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
        ('ED6_DT09/CH10610._CH', 'ED6_DT09/CH10610P._CP'),
        ('ED6_DT09/CH10611._CH', 'ED6_DT09/CH10611P._CP'),
        ('ED6_DT09/CH10080._CH', 'ED6_DT09/CH10080P._CP'),
        ('ED6_DT09/CH10081._CH', 'ED6_DT09/CH10081P._CP'),
        ('ED6_DT09/CH10120._CH', 'ED6_DT09/CH10120P._CP'),
        ('ED6_DT09/CH10121._CH', 'ED6_DT09/CH10121P._CP'),
        ('ED6_DT09/CH10140._CH', 'ED6_DT09/CH10140P._CP'),
        ('ED6_DT09/CH10141._CH', 'ED6_DT09/CH10141P._CP'),
        ('ED6_DT09/CH10620._CH', 'ED6_DT09/CH10620P._CP'),
        ('ED6_DT09/CH10621._CH', 'ED6_DT09/CH10621P._CP'),
        ('ED6_DT09/CH10600._CH', 'ED6_DT09/CH10600P._CP'),
        ('ED6_DT09/CH10601._CH', 'ED6_DT09/CH10601P._CP'),
        ('ED6_DT09/CH10400._CH', 'ED6_DT09/CH10400P._CP'),
        ('ED6_DT09/CH10401._CH', 'ED6_DT09/CH10401P._CP'),
        ('ED6_DT09/CH11210._CH', 'ED6_DT09/CH11210P._CP'),
        ('ED6_DT09/CH11211._CH', 'ED6_DT09/CH11211P._CP'),
        ('ED6_DT09/CH11250._CH', 'ED6_DT09/CH11250P._CP'),
        ('ED6_DT09/CH11251._CH', 'ED6_DT09/CH11251P._CP'),
    ]

# id: 0x10002 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 80,
            z                   = -10,
            y                   = -21790,
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
            x                   = 3840,
            z                   = -10,
            y                   = 156650,
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

# id: 0x10003 offset: 0x17A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 5200,
            z           = 10,
            y           = 19060,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0235,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -22900,
            z           = 10,
            y           = 49140,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0234,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6160,
            z           = -110,
            y           = 49360,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0234,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -23980,
            z           = -30,
            y           = 66400,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0232,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 8660,
            z           = -60,
            y           = 75740,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0235,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 18390,
            z           = 30,
            y           = 104990,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0232,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -6740,
            z           = -10,
            y           = 70020,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0232,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 4050,
            z           = 20,
            y           = 122400,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0234,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x25A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x25A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 16110,
            triggerZ            = -180,
            triggerY            = 115760,
            triggerRange        = 1000,
            actorX              = 16640,
            actorZ              = -180,
            actorY              = 116410,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -18750,
            triggerZ            = -20,
            triggerY            = 73400,
            triggerRange        = 1000,
            actorX              = -19250,
            actorZ              = -20,
            actorY              = 73900,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -14840,
            triggerZ            = -60,
            triggerY            = 20970,
            triggerRange        = 1000,
            actorX              = -15310,
            actorZ              = -60,
            actorY              = 20500,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x2C6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x2C7
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFE0430, 0xFFFEFE30, 0x00230036)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A2, 1, 0x1511)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2EB',
    )

    OP_6F(0x0000, 0)

    Jump('loc_2F2')

    def _loc_2EB(): pass

    label('loc_2EB')

    OP_6F(0x0000, 60)

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A2, 2, 0x1512)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_304',
    )

    OP_6F(0x0001, 0)

    Jump('loc_30B')

    def _loc_304(): pass

    label('loc_304')

    OP_6F(0x0001, 60)

    def _loc_30B(): pass

    label('loc_30B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A2, 3, 0x1513)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_31D',
    )

    OP_6F(0x0002, 0)

    Jump('loc_324')

    def _loc_31D(): pass

    label('loc_31D')

    OP_6F(0x0002, 60)

    def _loc_324(): pass

    label('loc_324')

    Return()

# id: 0x0002 offset: 0x325
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xF3, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A2, 1, 0x1511)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_402',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_399',
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
    OP_A2(0x1511)

    Jump('loc_3FF')

    def _loc_399(): pass

    label('loc_399')

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
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0x00000000)

    def _loc_3FF(): pass

    label('loc_3FF')

    Jump('loc_433')

    def _loc_402(): pass

    label('loc_402')

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
    def _loc_433(): pass

    label('loc_433')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x441
@scena.Code('func_03_441')
def func_03_441():
    UnlockAchievement(0x02, 0xF4, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A2, 2, 0x1512)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_51E',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['妨害２'], 1)"),
            Expr.Return,
        ),
        'loc_4B5',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['妨害２']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1512)

    Jump('loc_51B')

    def _loc_4B5(): pass

    label('loc_4B5')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['妨害２']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['妨害２']),
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

    def _loc_51B(): pass

    label('loc_51B')

    Jump('loc_54F')

    def _loc_51E(): pass

    label('loc_51E')

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
    def _loc_54F(): pass

    label('loc_54F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x55D
@scena.Code('func_04_55D')
def func_04_55D():
    UnlockAchievement(0x02, 0xF5, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A2, 3, 0x1513)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_63A',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['危险肉丸'], 1)"),
            Expr.Return,
        ),
        'loc_5D1',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['危险肉丸']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1513)

    Jump('loc_637')

    def _loc_5D1(): pass

    label('loc_5D1')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['危险肉丸']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['危险肉丸']),
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

    def _loc_637(): pass

    label('loc_637')

    Jump('loc_66B')

    def _loc_63A(): pass

    label('loc_63A')

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
    def _loc_66B(): pass

    label('loc_66B')

    Sleep(30)

    If(
        (
            (Expr.Eval, "OP_40(0x020D, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6C3',
    )

    If(
        (
            (Expr.Eval, "OP_AC(0x0028)"),
            Expr.Return,
        ),
        'loc_68A',
    )

    Jump('loc_6C3')

    def _loc_68A(): pass

    label('loc_68A')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['危险肉丸']),
            (TxtCtl.SetColor, 0x0),
            '的食谱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_22(0x0011, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['危险肉丸']),
            (TxtCtl.SetColor, 0x0),
            '的做法已经学会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6C3(): pass

    label('loc_6C3')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
