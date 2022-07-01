import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C3302_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3302   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
    TXT(0x02, ''),
    TXT(0x03, ''),
    TXT(0x04, ''),
    TXT(0x05, ''),
    TXT(0x06, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3302.x'
    header.mapIndex       = 1
    header.bgm            = 32
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x477
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
        ('ED6_DT09/CH10630._CH', 'ED6_DT09/CH10630P._CP'),
        ('ED6_DT09/CH10631._CH', 'ED6_DT09/CH10631P._CP'),
        ('ED6_DT09/CH10640._CH', 'ED6_DT09/CH10640P._CP'),
        ('ED6_DT09/CH10641._CH', 'ED6_DT09/CH10641P._CP'),
        ('ED6_DT09/CH10650._CH', 'ED6_DT09/CH10650P._CP'),
        ('ED6_DT09/CH10651._CH', 'ED6_DT09/CH10651P._CP'),
        ('ED6_DT09/CH10660._CH', 'ED6_DT09/CH10660P._CP'),
        ('ED6_DT09/CH10661._CH', 'ED6_DT09/CH10661P._CP'),
        ('ED6_DT09/CH10670._CH', 'ED6_DT09/CH10670P._CP'),
        ('ED6_DT09/CH10671._CH', 'ED6_DT09/CH10671P._CP'),
        ('ED6_DT09/CH10680._CH', 'ED6_DT09/CH10680P._CP'),
        ('ED6_DT09/CH10681._CH', 'ED6_DT09/CH10681P._CP'),
        ('ED6_DT09/CH10690._CH', 'ED6_DT09/CH10690P._CP'),
        ('ED6_DT09/CH10691._CH', 'ED6_DT09/CH10691P._CP'),
        ('ED6_DT09/CH10700._CH', 'ED6_DT09/CH10700P._CP'),
        ('ED6_DT09/CH10701._CH', 'ED6_DT09/CH10701P._CP'),
    ]

# id: 0x10002 offset: 0x12A
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0x12A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            x           = 30300,
            z           = 40,
            y           = -25110,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 9980,
            z           = 50,
            y           = -43520,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E5,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 29520,
            z           = -20,
            y           = 6960,
            word_0C     = 0x00B4,
            word_0E     = 0x000E,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E8,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -3210,
            z           = -10,
            y           = 11040,
            word_0C     = 0x00B4,
            word_0E     = 0x0000,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E1,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 12970,
            z           = -20,
            y           = 37620,
            word_0C     = 0x00B4,
            word_0E     = 0x0006,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x01E4,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x1B6
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1B6
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -8470,
            triggerZ            = 40,
            triggerY            = -39450,
            triggerRange        = 1000,
            actorX              = -9080,
            actorZ              = 1460,
            actorY              = -38880,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -5030,
            triggerZ            = -20,
            triggerY            = -16020,
            triggerRange        = 1000,
            actorX              = -5630,
            actorZ              = 1480,
            actorY              = -16340,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1FE
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1FF
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 7, 0x1537)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_211',
    )

    OP_6F(0x0000, 0)

    Jump('loc_218')

    def _loc_211(): pass

    label('loc_211')

    OP_6F(0x0000, 60)

    def _loc_218(): pass

    label('loc_218')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A7, 0, 0x1538)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_22A',
    )

    OP_6F(0x0001, 0)

    Jump('loc_231')

    def _loc_22A(): pass

    label('loc_22A')

    OP_6F(0x0001, 60)

    def _loc_231(): pass

    label('loc_231')

    OP_22(0x01CD, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x237
@scena.Code('ReInit')
def ReInit():
    UnlockAchievement(0x02, 0xBC, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A6, 7, 0x1537)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_314',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0000, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['川虫'], 1)"),
            Expr.Return,
        ),
        'loc_2AB',
    )

    FadeOut(300, 0, 100)
    OP_22(0x0011, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['川虫']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    OP_A2(0x1537)

    Jump('loc_311')

    def _loc_2AB(): pass

    label('loc_2AB')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['川虫']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['川虫']),
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

    def _loc_311(): pass

    label('loc_311')

    Jump('loc_345')

    def _loc_314(): pass

    label('loc_314')

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
    def _loc_345(): pass

    label('loc_345')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x353
@scena.Code('func_03_353')
def func_03_353():
    UnlockAchievement(0x02, 0xBD, 0x00, 0x00)
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02A7, 0, 0x1538)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_430',
    )

    OP_22(0x002B, 0x00, 0x64)
    OP_70(0x0001, 0x0000003C)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['中回复药'], 1)"),
            Expr.Return,
        ),
        'loc_3C7',
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
    OP_A2(0x1538)

    Jump('loc_42D')

    def _loc_3C7(): pass

    label('loc_3C7')

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

    def _loc_42D(): pass

    label('loc_42D')

    Jump('loc_461')

    def _loc_430(): pass

    label('loc_430')

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
    def _loc_461(): pass

    label('loc_461')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
