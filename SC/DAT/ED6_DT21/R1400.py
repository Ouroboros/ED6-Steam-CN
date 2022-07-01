import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1400   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '柏斯方向'),
    TXT(0x02, '瓦雷利亚湖畔方向'),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
    TXT(0x07, ''),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1400.x'
    header.mapIndex       = 58
    header.bgm            = 29
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x660
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
        ('ED6_DT09/CH10290._CH', 'ED6_DT09/CH10290P._CP'),
        ('ED6_DT09/CH10291._CH', 'ED6_DT09/CH10291P._CP'),
        ('ED6_DT09/CH10310._CH', 'ED6_DT09/CH10310P._CP'),
        ('ED6_DT09/CH10311._CH', 'ED6_DT09/CH10311P._CP'),
        ('ED6_DT09/CH10320._CH', 'ED6_DT09/CH10320P._CP'),
        ('ED6_DT09/CH10321._CH', 'ED6_DT09/CH10321P._CP'),
        ('ED6_DT09/CH10350._CH', 'ED6_DT09/CH10350P._CP'),
        ('ED6_DT09/CH10351._CH', 'ED6_DT09/CH10351P._CP'),
        ('ED6_DT09/CH10540._CH', 'ED6_DT09/CH10540P._CP'),
        ('ED6_DT09/CH10541._CH', 'ED6_DT09/CH10541P._CP'),
        ('ED6_DT09/CH10550._CH', 'ED6_DT09/CH10550P._CP'),
        ('ED6_DT09/CH10551._CH', 'ED6_DT09/CH10551P._CP'),
        ('ED6_DT09/CH10870._CH', 'ED6_DT09/CH10870P._CP'),
        ('ED6_DT09/CH10871._CH', 'ED6_DT09/CH10871P._CP'),
    ]

# id: 0x10002 offset: 0x11A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -153950,
            z                   = 0,
            y                   = 68430,
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
            x                   = -140970,
            z                   = -10,
            y                   = -85530,
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

# id: 0x10003 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -159990,
            z           = 0,
            y           = 15330,
            word_0C     = 0x0000,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x011E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -162450,
            z           = -30,
            y           = 220,
            word_0C     = 0x0000,
            word_0E     = 0x000A,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x011F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -181290,
            z           = 50,
            y           = -41120,
            word_0C     = 0x0000,
            word_0E     = 0x000C,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0120,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -147870,
            z           = 20,
            y           = -37440,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0119,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -132980,
            z           = 0,
            y           = -60680,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x011A,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1E6
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1E6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -156160,
            triggerZ            = 20,
            triggerY            = -10160,
            triggerRange        = 1000,
            actorX              = -155470,
            actorZ              = 20,
            actorY              = -10210,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -166090,
            triggerZ            = -220,
            triggerY            = -6880,
            triggerRange        = 1000,
            actorX              = -166670,
            actorZ              = -220,
            actorY              = -6930,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -151930,
            triggerZ            = 360,
            triggerY            = -34470,
            triggerRange        = 1000,
            actorX              = -151180,
            actorZ              = 360,
            actorY              = -34380,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -160560,
            triggerZ            = 0,
            triggerY            = 35590,
            triggerRange        = 1500,
            actorX              = -160560,
            actorZ              = 1500,
            actorY              = 35590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x276
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x277
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFB9EE8, 0xFFFDF878, 0x0023001C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0368, 2, 0x1B42)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_29B',
    )

    OP_6F(0x0001, 0)

    Jump('loc_2A2')

    def _loc_29B(): pass

    label('loc_29B')

    OP_6F(0x0001, 60)

    def _loc_2A2(): pass

    label('loc_2A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0368, 3, 0x1B43)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B4',
    )

    OP_6F(0x0002, 0)

    Jump('loc_2BB')

    def _loc_2B4(): pass

    label('loc_2B4')

    OP_6F(0x0002, 60)

    def _loc_2BB(): pass

    label('loc_2BB')

    OP_64(0x00, 0x0001)
    OP_71(0x0000, 0x0000)
    OP_71(0x0000, 0x0004)

    Return()

# id: 0x0002 offset: 0x2CA
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2DF',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('ReInit')

    def _loc_2DF(): pass

    label('loc_2DF')

    Return()

# id: 0x0003 offset: 0x2E0
@scena.Code('func_03_2E0')
def func_03_2E0():
    UnlockAchievement(0x02, 0xD0, 0x01, 0x00)
    SetMapFlags(0x08000000)
    FadeOut(300, 0, 100)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0368, 0, 0x1B40)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_392',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000001E)
    OP_73(0x0000)
    OP_6F(0x0000, 30)
    AddSepith(0x04, 0x0032)
    AddSepith(0x05, 0x0032)
    AddSepith(0x06, 0x0032)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '#62I时之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x2),
            '#60I空之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x2),
            '#61I幻之耀晶片×５０\n',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1B40)

    Jump('loc_3AC')

    def _loc_392(): pass

    label('loc_392')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱中什么都没有。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)

    def _loc_3AC(): pass

    label('loc_3AC')

    FadeIn(300, 0)
    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x3BE
@scena.Code('func_04_3BE')
def func_04_3BE():
    UnlockAchievement(0x02, 0xD1, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0368, 2, 0x1B42)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_49B',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_432',
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
    OP_A2(0x1B42)

    Jump('loc_498')

    def _loc_432(): pass

    label('loc_432')

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

    def _loc_498(): pass

    label('loc_498')

    Jump('loc_4CC')

    def _loc_49B(): pass

    label('loc_49B')

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
    def _loc_4CC(): pass

    label('loc_4CC')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x4DA
@scena.Code('func_05_4DA')
def func_05_4DA():
    UnlockAchievement(0x02, 0xD2, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0368, 3, 0x1B43)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5B7',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0002, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['活性之药'], 1)"),
            Expr.Return,
        ),
        'loc_54E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B43)

    Jump('loc_5B4')

    def _loc_54E(): pass

    label('loc_54E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['活性之药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['活性之药']),
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

    def _loc_5B4(): pass

    label('loc_5B4')

    Jump('loc_5E8')

    def _loc_5B7(): pass

    label('loc_5B7')

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
    def _loc_5E8(): pass

    label('loc_5E8')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0006 offset: 0x5F6
@scena.Code('func_06_5F6')
def func_06_5F6():
    FadeOut(300, 0, 100)
    SetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　柏斯市\n',
            '南　瓦雷利亚湖畔　２００塞尔矩',
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
