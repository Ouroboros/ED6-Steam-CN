import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import C0415_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0415   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0415.x'
    header.mapIndex       = 1
    header.bgm            = 33
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT09/CH10040._CH', 'ED6_DT09/CH10040P._CP'),
        ('ED6_DT09/CH10041._CH', 'ED6_DT09/CH10041P._CP'),
        ('ED6_DT09/CH10070._CH', 'ED6_DT09/CH10070P._CP'),
        ('ED6_DT09/CH10071._CH', 'ED6_DT09/CH10071P._CP'),
        ('ED6_DT09/CH10150._CH', 'ED6_DT09/CH10150P._CP'),
        ('ED6_DT09/CH10151._CH', 'ED6_DT09/CH10151P._CP'),
        ('ED6_DT09/CH10190._CH', 'ED6_DT09/CH10190P._CP'),
        ('ED6_DT09/CH10191._CH', 'ED6_DT09/CH10191P._CP'),
        ('ED6_DT29/CH12140._CH', 'ED6_DT29/CH12140P._CP'),
        ('ED6_DT29/CH12141._CH', 'ED6_DT29/CH12141P._CP'),
    ]

# id: 0x10001 offset: 0xFA
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xFA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = 12510,
            z           = 0,
            y           = -10,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x197B,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -12570,
            z           = 0,
            y           = -30,
            word_0C     = 0x00B4,
            word_0E     = 0x0004,
            byte_10     = 0x41,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0034,
            word_18     = 0x197C,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x132
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x132
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -8590,
            triggerZ            = 0,
            triggerY            = -9040,
            triggerRange        = 1000,
            actorX              = -8150,
            actorZ              = 0,
            actorY              = -9480,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -4360,
            triggerZ            = 0,
            triggerY            = 22580,
            triggerRange        = 1000,
            actorX              = -4450,
            actorZ              = 0,
            actorY              = 23190,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 4390,
            triggerZ            = 0,
            triggerY            = 22620,
            triggerRange        = 1000,
            actorX              = 4430,
            actorZ              = 0,
            actorY              = 23230,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x19E
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0x19F
@scena.Code('func_01_19F')
def func_01_19F():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032B, 0, 0x1958)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1B1',
    )

    OP_6F(0x0000, 0)

    Jump('loc_1B8')

    def _loc_1B1(): pass

    label('loc_1B1')

    OP_6F(0x0000, 60)

    def _loc_1B8(): pass

    label('loc_1B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032B, 2, 0x195A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1CA',
    )

    OP_6F(0x0001, 0)

    Jump('loc_1D1')

    def _loc_1CA(): pass

    label('loc_1CA')

    OP_6F(0x0001, 60)

    def _loc_1D1(): pass

    label('loc_1D1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032B, 4, 0x195C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E3',
    )

    OP_6F(0x0002, 0)

    Jump('loc_1EA')

    def _loc_1E3(): pass

    label('loc_1E3')

    OP_6F(0x0002, 60)

    def _loc_1EA(): pass

    label('loc_1EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032F, 3, 0x197B)),
            Expr.Return,
        ),
        'loc_1F6',
    )

    ChrSetFlags(0x0008, 0x0080)

    def _loc_1F6(): pass

    label('loc_1F6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032F, 4, 0x197C)),
            Expr.Return,
        ),
        'loc_202',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_202(): pass

    label('loc_202')

    Return()

# id: 0x0002 offset: 0x203
@scena.Code('func_02_203')
def func_02_203():
    UnlockAchievement(0x02, 0x0010, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032B, 0, 0x1958)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E0',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0000, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['金刚杖'], 1)"),
            Expr.Return,
        ),
        'loc_277',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['金刚杖']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032B, 0, 0x1958))

    Jump('loc_2DD')

    def _loc_277(): pass

    label('loc_277')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['金刚杖']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['金刚杖']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0000, 60)
    OP_70(0x0000, 0)

    def _loc_2DD(): pass

    label('loc_2DD')

    Jump('loc_311')

    def _loc_2E0(): pass

    label('loc_2E0')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_311(): pass

    label('loc_311')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0003 offset: 0x31F
@scena.Code('func_03_31F')
def func_03_31F():
    UnlockAchievement(0x02, 0x0011, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032B, 2, 0x195A)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_3FC',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['魔力鞋'], 1)"),
            Expr.Return,
        ),
        'loc_393',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['魔力鞋']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032B, 2, 0x195A))

    Jump('loc_3F9')

    def _loc_393(): pass

    label('loc_393')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['魔力鞋']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['魔力鞋']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_3F9(): pass

    label('loc_3F9')

    Jump('loc_42D')

    def _loc_3FC(): pass

    label('loc_3FC')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_42D(): pass

    label('loc_42D')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x43B
@scena.Code('func_04_43B')
def func_04_43B():
    UnlockAchievement(0x02, 0x0012, 0x00)
    MapSetFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x032B, 4, 0x195C)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_518',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(ItemTable['魔防４'], 1)"),
            Expr.Return,
        ),
        'loc_4AF',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.Item, ItemTable['魔防４']),
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x032B, 4, 0x195C))

    Jump('loc_515')

    def _loc_4AF(): pass

    label('loc_4AF')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.Item, ItemTable['魔防４']),
            (TxtCtl.SetColor, 0x0),
            '。   \n',
            '所持物品已经满了，',
            (TxtCtl.Item, ItemTable['魔防４']),
            (TxtCtl.SetColor, 0x0),
            '只能放弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_515(): pass

    label('loc_515')

    Jump('loc_549')

    def _loc_518(): pass

    label('loc_518')

    FadeOut(300, 0, 100)
    TalkSetChrName('')

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
    def _loc_549(): pass

    label('loc_549')

    Sleep(30)

    TalkEnd(0x00FF)
    MapClearFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
