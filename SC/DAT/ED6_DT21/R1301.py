import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import R1301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R1301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '东柏斯街道方向'),
    TXT(0x02, '哈肯大门方向'),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'R1301.x'
    header.mapIndex       = 57
    header.bgm            = 22
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x42C
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
        ('ED6_DT09/CH10370._CH', 'ED6_DT09/CH10370P._CP'),
        ('ED6_DT09/CH10371._CH', 'ED6_DT09/CH10371P._CP'),
        ('ED6_DT09/CH10360._CH', 'ED6_DT09/CH10360P._CP'),
        ('ED6_DT09/CH10361._CH', 'ED6_DT09/CH10361P._CP'),
    ]

# id: 0x10002 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -204170,
            z                   = 20,
            y                   = 10080,
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
            x                   = -222100,
            z                   = 10,
            y                   = 149520,
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

# id: 0x10003 offset: 0x10A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = -215110,
            z           = 0,
            y           = 47900,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0106,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -212230,
            z           = 10,
            y           = 71070,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0105,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -214830,
            z           = -50,
            y           = 109950,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0106,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x15E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x15E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -220630,
            triggerZ            = -190,
            triggerY            = 85710,
            triggerRange        = 1000,
            actorX              = -221300,
            actorZ              = -190,
            actorY              = 85710,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -203450,
            triggerZ            = -30,
            triggerY            = 57000,
            triggerRange        = 1000,
            actorX              = -202740,
            actorZ              = -30,
            actorY              = 57050,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1A6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1A7
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFACBF8, 0xFFFF63C0, 0x00230014)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 2, 0x1B12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CB',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1D2')

    def _loc_1CB(): pass

    label('loc_1CB')

    OP_6F(0x0000, 60)

    def _loc_1D2(): pass

    label('loc_1D2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 3, 0x1B13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E4',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1EB')

    def _loc_1E4(): pass

    label('loc_1E4')

    OP_6F(0x0001, 60)

    def _loc_1EB(): pass

    label('loc_1EB')

    Return()

# id: 0x0002 offset: 0x1EC
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xCE, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 2, 0x1B12)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2C9',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['蚯蚓'], 1)"),
            Expr.Return,
        ),
        'loc_260',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['蚯蚓']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1B12)

    Jump('loc_2C6')

    def _loc_260(): pass

    label('loc_260')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['蚯蚓']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['蚯蚓']),
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

    def _loc_2C6(): pass

    label('loc_2C6')

    Jump('loc_2FA')

    def _loc_2C9(): pass

    label('loc_2C9')

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
    def _loc_2FA(): pass

    label('loc_2FA')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x308
@scena.Code('func_03_308')
def func_03_308():
    UnlockAchievement(0x02, 0xCF, 0x01, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0362, 3, 0x1B13)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3E5',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['复苏药'], 1)"),
            Expr.Return,
        ),
        'loc_37C',
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
    OP_A2(0x1B13)

    Jump('loc_3E2')

    def _loc_37C(): pass

    label('loc_37C')

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
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0x00000000)

    def _loc_3E2(): pass

    label('loc_3E2')

    Jump('loc_416')

    def _loc_3E5(): pass

    label('loc_3E5')

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
    def _loc_416(): pass

    label('loc_416')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
