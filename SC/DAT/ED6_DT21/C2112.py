import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C2112_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C2112   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'C2112.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x41E
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
        ('ED6_DT09/CH10560._CH', 'ED6_DT09/CH10560P._CP'),
        ('ED6_DT09/CH10561._CH', 'ED6_DT09/CH10561P._CP'),
        ('ED6_DT09/CH10570._CH', 'ED6_DT09/CH10570P._CP'),
        ('ED6_DT09/CH10571._CH', 'ED6_DT09/CH10571P._CP'),
        ('ED6_DT09/CH10580._CH', 'ED6_DT09/CH10580P._CP'),
        ('ED6_DT09/CH10581._CH', 'ED6_DT09/CH10581P._CP'),
        ('ED6_DT09/CH10590._CH', 'ED6_DT09/CH10590P._CP'),
        ('ED6_DT09/CH10591._CH', 'ED6_DT09/CH10591P._CP'),
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
            x           = -150,
            z           = 0,
            y           = -10,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01B9,
            word_18     = 0x1351,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 21120,
            z           = 0,
            y           = 3940,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01BB,
            word_18     = 0x1352,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -21420,
            z           = 0,
            y           = 3700,
            word_0C     = 0x00B4,
            word_0E     = 0x0002,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01BA,
            word_18     = 0x1353,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x13E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x13E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -21770,
            triggerZ            = 0,
            triggerY            = -2940,
            triggerRange        = 1000,
            actorX              = -21820,
            actorZ              = 0,
            actorY              = -3560,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 22320,
            triggerZ            = 0,
            triggerY            = -80,
            triggerRange        = 1000,
            actorX              = 22880,
            actorZ              = 0,
            actorY              = -170,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x186
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x187
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 0, 0x1310)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_199',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1A0')

    def _loc_199(): pass

    label('loc_199')

    OP_6F(0x0000, 60)

    def _loc_1A0(): pass

    label('loc_1A0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 1, 0x1311)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B2',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1B9')

    def _loc_1B2(): pass

    label('loc_1B2')

    OP_6F(0x0001, 60)

    def _loc_1B9(): pass

    label('loc_1B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x026A, 1, 0x1351)),
            Expr.Return,
        ),
        'loc_1C5',
    )

    SetChrFlags(0x0008, 0x0080)

    def _loc_1C5(): pass

    label('loc_1C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x026A, 2, 0x1352)),
            Expr.Return,
        ),
        'loc_1D1',
    )

    SetChrFlags(0x0009, 0x0080)

    def _loc_1D1(): pass

    label('loc_1D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x026A, 3, 0x1353)),
            Expr.Return,
        ),
        'loc_1DD',
    )

    SetChrFlags(0x000A, 0x0080)

    def _loc_1DD(): pass

    label('loc_1DD')

    Return()

# id: 0x0002 offset: 0x1DE
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0x85, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 0, 0x1310)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2BB',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['回复药'], 1)"),
            Expr.Return,
        ),
        'loc_252',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1310)

    Jump('loc_2B8')

    def _loc_252(): pass

    label('loc_252')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['回复药']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['回复药']),
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

    def _loc_2B8(): pass

    label('loc_2B8')

    Jump('loc_2EC')

    def _loc_2BB(): pass

    label('loc_2BB')

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
    def _loc_2EC(): pass

    label('loc_2EC')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x2FA
@scena.Code('func_03_2FA')
def func_03_2FA():
    UnlockAchievement(0x02, 0x86, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0262, 1, 0x1311)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3D7',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['虾米'], 1)"),
            Expr.Return,
        ),
        'loc_36E',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['虾米']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1311)

    Jump('loc_3D4')

    def _loc_36E(): pass

    label('loc_36E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['虾米']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['虾米']),
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

    def _loc_3D4(): pass

    label('loc_3D4')

    Jump('loc_408')

    def _loc_3D7(): pass

    label('loc_3D7')

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
    def _loc_408(): pass

    label('loc_408')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
