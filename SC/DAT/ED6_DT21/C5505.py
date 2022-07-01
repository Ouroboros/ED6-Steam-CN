import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C5505_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C5505   ._SN')

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
    header.mapName        = 'Other'
    header.mapModel       = 'C5505.x'
    header.mapIndex       = 1
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x5B5
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
        ('ED6_DT29/CH12180._CH', 'ED6_DT29/CH12180P._CP'),
        ('ED6_DT29/CH12181._CH', 'ED6_DT29/CH12181P._CP'),
        ('ED6_DT29/CH12230._CH', 'ED6_DT29/CH12230P._CP'),
        ('ED6_DT29/CH12231._CH', 'ED6_DT29/CH12231P._CP'),
        ('ED6_DT29/CH12270._CH', 'ED6_DT29/CH12270P._CP'),
        ('ED6_DT29/CH12271._CH', 'ED6_DT29/CH12271P._CP'),
        ('ED6_DT29/CH12360._CH', 'ED6_DT29/CH12360P._CP'),
        ('ED6_DT29/CH12361._CH', 'ED6_DT29/CH12361P._CP'),
    ]

# id: 0x10002 offset: 0xEA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -26690,
            z                   = 1000,
            y                   = 13420,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -26150,
            z           = 0,
            y           = -18160,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -9050,
            z           = 0,
            y           = -1650,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 350,
            z           = 0,
            y           = -14310,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0389,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 37130,
            z           = 0,
            y           = -6030,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 16500,
            z           = 0,
            y           = 22960,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0389,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -24260,
            z           = 0,
            y           = 2230,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -32920,
            z           = 0,
            y           = 21400,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x038C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1CE
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1CE
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 40970,
            triggerZ            = 0,
            triggerY            = -12100,
            triggerRange        = 1000,
            actorX              = 41400,
            actorZ              = 0,
            actorY              = -12530,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -26690,
            triggerZ            = 0,
            triggerY            = 14080,
            triggerRange        = 1000,
            actorX              = -26690,
            actorZ              = 0,
            actorY              = 13420,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x216
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x217
@scena.Code('Init')
def Init():
    OP_22(0x01CD, 0x00, 0x64)
    OP_22(0x01CE, 0x01, 0x50)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 1, 0x1121)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_233',
    )

    OP_6F(0x0000, 0)

    Jump('loc_23A')

    def _loc_233(): pass

    label('loc_233')

    OP_6F(0x0000, 60)

    def _loc_23A(): pass

    label('loc_23A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 2, 0x1122)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24C',
    )

    OP_6F(0x0001, 0)

    Jump('loc_253')

    def _loc_24C(): pass

    label('loc_24C')

    OP_6F(0x0001, 60)

    def _loc_253(): pass

    label('loc_253')

    Return()

# id: 0x0002 offset: 0x254
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_269',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_269(): pass

    label('loc_269')

    Return()

# id: 0x0003 offset: 0x26A
@scena.Code('func_03_26A')
def func_03_26A():
    UnlockAchievement(0x02, 0x8F, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 1, 0x1121)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_347',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['强化皮靴'], 1)"),
            Expr.Return,
        ),
        'loc_2DE',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['强化皮靴']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1121)

    Jump('loc_344')

    def _loc_2DE(): pass

    label('loc_2DE')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['强化皮靴']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['强化皮靴']),
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

    def _loc_344(): pass

    label('loc_344')

    Jump('loc_378')

    def _loc_347(): pass

    label('loc_347')

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
    def _loc_378(): pass

    label('loc_378')

    Sleep(30)

    Call(0, 0x0005)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x38A
@scena.Code('func_04_38A')
def func_04_38A():
    UnlockAchievement(0x02, 0x90, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0224, 2, 0x1122)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_467',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['强化皮铠'], 1)"),
            Expr.Return,
        ),
        'loc_3FE',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['强化皮铠']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1122)

    Jump('loc_464')

    def _loc_3FE(): pass

    label('loc_3FE')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['强化皮铠']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['强化皮铠']),
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

    def _loc_464(): pass

    label('loc_464')

    Jump('loc_498')

    def _loc_467(): pass

    label('loc_467')

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
    def _loc_498(): pass

    label('loc_498')

    Sleep(30)

    Call(0, 0x0005)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x4AA
@scena.Code('func_05_4AA')
def func_05_4AA():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0201, 7, 0x100F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5A8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010191230V#1004F啊……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010191231V难不成，这个\n',
            '就是我们的装备？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x010A,
        (
            '#0120191232V#811F嗯，似乎是呢⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0120191233V#1310F说不定其它装备\n',
            '也被藏在什么地方了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010191234V#1006F嗯～\n',
            '虽然想避开和魔兽的战斗，\n',
            '但似乎值得探索一下呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x100F)

    def _loc_5A8(): pass

    label('loc_5A8')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
