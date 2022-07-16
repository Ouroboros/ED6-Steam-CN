import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C0300_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C0300   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '森林之雾'),
    TXT(0x02, '森林之雾'),
    TXT(0x03, '菠萝怪'),
    TXT(0x04, '菠萝怪'),
    TXT(0x05, '巨型雪猿'),
    TXT(0x06, '巨型雪猿'),
    TXT(0x07, '巨型雪猿'),
    TXT(0x08, '巨型雪猿'),
    TXT(0x09, '巨型雪猿'),
    TXT(0x0A, '巨型雪猿'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0300.x'
    header.mapIndex       = 19
    header.bgm            = 21
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x719
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00004E20,
            dword_04        = 0x00000000,
            dword_08        = 0x00004268,
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
        ('ED6_DT09/CH10010._CH', 'ED6_DT09/CH10010P._CP'),
        ('ED6_DT09/CH10011._CH', 'ED6_DT09/CH10011P._CP'),
        ('ED6_DT09/CH10280._CH', 'ED6_DT09/CH10280P._CP'),
        ('ED6_DT09/CH10281._CH', 'ED6_DT09/CH10281P._CP'),
        ('ED6_DT09/CH10230._CH', 'ED6_DT09/CH10230P._CP'),
        ('ED6_DT09/CH10231._CH', 'ED6_DT09/CH10231P._CP'),
        ('ED6_DT09/CH10240._CH', 'ED6_DT09/CH10240P._CP'),
        ('ED6_DT09/CH10241._CH', 'ED6_DT09/CH10241P._CP'),
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
            x           = -24000,
            z           = 0,
            y           = -7000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0042,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -10000,
            z           = 0,
            y           = 17000,
            word_0C     = 0x0000,
            word_0E     = 0x0002,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0042,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 24000,
            z           = 0,
            y           = 33000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0044,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -12000,
            z           = 0,
            y           = 51000,
            word_0C     = 0x0000,
            word_0E     = 0x0004,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0050,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -16000,
            z           = 0,
            y           = -20000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -14000,
            z           = 0,
            y           = -8000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x003F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -3000,
            z           = 0,
            y           = 32000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0040,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -15000,
            z           = 0,
            y           = 8000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0040,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = 11000,
            z           = 0,
            y           = 18000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0040,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -14000,
            z           = 0,
            y           = 37000,
            word_0C     = 0x0000,
            word_0E     = 0x0000,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0040,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x202
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x202
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 28180,
            triggerZ            = 0,
            triggerY            = 33590,
            triggerRange        = 1500,
            actorX              = 28180,
            actorZ              = 1500,
            actorY              = 33590,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 21340,
            triggerZ            = -170,
            triggerY            = 17550,
            triggerRange        = 1000,
            actorX              = 22310,
            actorZ              = 1340,
            actorY              = 17540,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0004,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x24A
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_256'),
        (-1, 'loc_269'),
    )

    def _loc_256(): pass

    label('loc_256')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 5, 0x265)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x004C, 4, 0x264)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_266',
    )

    Event(0, 0x0002)

    def _loc_266(): pass

    label('loc_266')

    Jump('loc_269')

    def _loc_269(): pass

    label('loc_269')

    Return()

# id: 0x0001 offset: 0x26A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0052, 2, 0x292)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_27C',
    )

    OP_6F(0x0002, 0)

    Jump('loc_283')

    def _loc_27C(): pass

    label('loc_27C')

    OP_6F(0x0002, 60)

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 7, 0x287)),
            Expr.Return,
        ),
        'loc_298',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    OP_64(0x00, 0x0001)

    def _loc_298(): pass

    label('loc_298')

    Return()

# id: 0x0002 offset: 0x299
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x004C, 5, 0x265))
    CameraMove(-19820, 80, -24370, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(0, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -18840, -230, -46470, 0)
    SetChrPos(0x0102, -20460, -330, -47080, 0)
    SetChrPos(0x0103, -19740, -300, -45510, 0)
    FadeIn(1000, 0)
    CameraMove(-19740, -320, -44250, 5000)

    ChrTalk(
        0x0101,
        (
            '#0010011215V#002F这里就是神秘森林啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)
    ChrTurnDirection(0x0102, 0x0103, 400)

    ChrTalk(
        0x0102,
        (
            '#0020011216V#012F雪拉姐姐，能看出什么来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011217V#026F#2P………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0103, 180, 400)

    ChrTalk(
        0x0103,
        (
            '#0030011218V#022F#2P……没错了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011219V#022F看得出来不久之前\n',
            '有好几个人从这里通过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011220V#022F十有八九是料中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011221V#004F这、这也能看出来吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030011222V#020F#2P追踪逃走的犯人\n',
            '也是游击士必要的技能呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030011223V#020F总之我们进森林里调查一下吧。\n',
            '注意不要发出太大的声音哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010011224V#006F知道～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020011225V#012F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x510
@scena.Code('func_03_510')
def func_03_510():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0050, 7, 0x287)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_5D1',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x0386, 1)"),
            Expr.Return,
        ),
        'loc_57F',
    )

    OP_71(0x0000, 0x0004)
    OP_71(0x0001, 0x0004)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x0050, 7, 0x287))

    Jump('loc_5D1')

    def _loc_57F(): pass

    label('loc_57F')

    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '熊刺草',
            (TxtCtl.SetColor, 0x0),
            '发现了，\n',
            (TxtCtl.SetColor, 0x0),
            '不过现有的数量太多，不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_5D1(): pass

    label('loc_5D1')

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0004 offset: 0x5DA
@scena.Code('func_04_5DA')
def func_04_5DA():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0052, 2, 0x292)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6C4',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0002, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F5, 1)"),
            Expr.Return,
        ),
        'loc_64E',
    )

    FadeOut(300, 0, 100)
    PlaySE(17, 0x00, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x0052, 2, 0x292))

    Jump('loc_6C1')

    def _loc_64E(): pass

    label('loc_64E')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0002, 60)
    OP_70(0x0002, 0)

    def _loc_6C1(): pass

    label('loc_6C1')

    Jump('loc_6FC')

    def _loc_6C4(): pass

    label('loc_6C4')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '宝箱里什么东西都没有。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    WaitEffect(0x0F, 0x01)
    def _loc_6FC(): pass

    label('loc_6FC')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

# id: 0x0005 offset: 0x70A
@scena.Code('func_05_70A')
def func_05_70A():
    EventBegin(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
