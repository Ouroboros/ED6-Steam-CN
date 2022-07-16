import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4203   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4203.x'
    header.mapIndex       = 1
    header.bgm            = 31
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x725
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
        ('ED6_DT09/CH10490._CH', 'ED6_DT09/CH10490P._CP'),
        ('ED6_DT09/CH10491._CH', 'ED6_DT09/CH10491P._CP'),
        ('ED6_DT09/CH10500._CH', 'ED6_DT09/CH10500P._CP'),
        ('ED6_DT09/CH10501._CH', 'ED6_DT09/CH10501P._CP'),
        ('ED6_DT09/CH10510._CH', 'ED6_DT09/CH10510P._CP'),
        ('ED6_DT09/CH10511._CH', 'ED6_DT09/CH10511P._CP'),
        ('ED6_DT09/CH11110._CH', 'ED6_DT09/CH11110P._CP'),
        ('ED6_DT09/CH11111._CH', 'ED6_DT09/CH11111P._CP'),
        ('ED6_DT09/CH11120._CH', 'ED6_DT09/CH11120P._CP'),
        ('ED6_DT09/CH11121._CH', 'ED6_DT09/CH11121P._CP'),
        ('ED6_DT09/CH11130._CH', 'ED6_DT09/CH11130P._CP'),
        ('ED6_DT09/CH11131._CH', 'ED6_DT09/CH11131P._CP'),
        ('ED6_DT09/CH11140._CH', 'ED6_DT09/CH11140P._CP'),
        ('ED6_DT09/CH11141._CH', 'ED6_DT09/CH11141P._CP'),
        ('ED6_DT09/CH11150._CH', 'ED6_DT09/CH11150P._CP'),
        ('ED6_DT09/CH11151._CH', 'ED6_DT09/CH11151P._CP'),
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
            x           = -47360,
            z           = 0,
            y           = 42620,
            word_0C     = 0x00B4,
            word_0E     = 0x000A,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -121330,
            z           = 0,
            y           = 50600,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x0277,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            x           = -88180,
            z           = 0,
            y           = 51510,
            word_0C     = 0x00B4,
            word_0E     = 0x0008,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x027F,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10004 offset: 0x17E
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x17E
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -101030,
            triggerZ            = 0,
            triggerY            = 62030,
            triggerRange        = 800,
            actorX              = -101030,
            actorZ              = 500,
            actorY              = 62030,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -91330,
            triggerZ            = 0,
            triggerY            = 60050,
            triggerRange        = 1000,
            actorX              = -91210,
            actorZ              = 1500,
            actorY              = 60790,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1C6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0x1C7
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 5, 0x65D)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_1D7',
    )

    OP_64(0x00, 0x0001)

    def _loc_1D7(): pass

    label('loc_1D7')

    OP_72(0x0000, 0x0010)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 5, 0x65D)),
            Expr.Return,
        ),
        'loc_1EA',
    )

    OP_6F(0x0000, 240)

    def _loc_1EA(): pass

    label('loc_1EA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 5, 0x6DD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1FC',
    )

    OP_6F(0x0001, 0)

    Jump('loc_203')

    def _loc_1FC(): pass

    label('loc_1FC')

    OP_6F(0x0001, 60)

    def _loc_203(): pass

    label('loc_203')

    PlaySE(461, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x209
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    CameraMove(-100990, 0, 62230, 1000)

    ChrTalk(
        0x0102,
        (
            '#0020131029V#010F这一带就是地图上\n',
            '标有『＝』的地点了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131030V#073F嗯，仔细一看竟然\n',
            '没有任何机关之类的痕迹……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131031V不愧是出自王家之手的设计啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040131032V#035F看来得从上到下，从左到右，\n',
            '里里外外全部调查一遍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020131033V#012F……我先来试试看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0102, -101200, 0, 61500, 0)
    SetChrPos(0x0108, -100610, 0, 59330, 0)
    SetChrPos(0x0104, -101480, 0, 59880, 0)
    Sleep(500)

    FadeIn(1000, 0)
    OP_0D()
    ChrMoveTo(0x0102, -100530, 0, 61450, 700, 0x00)
    Sleep(500)

    ChrMoveTo(0x0102, -101490, 0, 61370, 500, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020131034V#015F嗯……这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(500)

    PlaySE(100, 0x00, 0x64)
    Sleep(500)

    OP_71(0x0000, 0x0010)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 120)
    PlaySE(112, 0x00, 0x64)
    OP_73(0x0000)
    OP_6F(0x0000, 120)
    OP_70(0x0000, 240)
    PlaySE(112, 0x00, 0x64)

    ChrTalk(
        0x0108,
        (
            '#0080131035V#071F太棒了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040131036V#033F哦，很厉害嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131037V这样的设计有什么寻找的窍门可言吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0104, 400)

    ChrTalk(
        0x0102,
        (
            '#0020131038V#013F#5P要说窍门……\n',
            '只是简单的惯性思维而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020131039V#010F很自然的用指尖摸索一下就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040131040V#030F很自然的啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131041V#031F约修亚君，你难道就是\n',
            '当年那位传说中的少年怪盗吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040131042V就像武打片里面那些角色一样哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020131043V#018F#5P我说你啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080131044V#070F没时间了。我们赶快行动吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080131045V从现在开始就要动真格了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_73(0x0000)
    OP_72(0x0000, 0x0010)
    OP_71(0x0000, 0x0002)
    OP_64(0x00, 0x0001)
    SetScenaFlags(ScenaFlag(0x00CB, 5, 0x65D))
    OP_28(0x004D, 0x01, 0x0008)
    OP_28(0x004D, 0x01, 0x0010)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x5E9
@scena.Code('func_03_5E9')
def func_03_5E9():
    SetMapFlags(0x08000000)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00DB, 5, 0x6DD)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D9',
    )

    PlaySE(43, 0x00, 0x64)
    OP_70(0x0001, 60)
    Sleep(500)

    If(
        (
            (Expr.Eval, "AddItem(0x01F6, 1)"),
            Expr.Return,
        ),
        'loc_65F',
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
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    SetScenaFlags(ScenaFlag(0x00DB, 5, 0x6DD))

    Jump('loc_6D6')

    def _loc_65F(): pass

    label('loc_65F')

    FadeOut(300, 0, 100)
    SetChrName('')

    Talk(
        (
            '宝箱里装有',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '。\n',
            '不过现有的数量太多，',
            (TxtCtl.SetColor, 0x2),
            '大回复药',
            (TxtCtl.SetColor, 0x0),
            '不能再拿更多了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    PlaySE(44, 0x00, 0x64)
    OP_6F(0x0001, 60)
    OP_70(0x0001, 0)

    def _loc_6D6(): pass

    label('loc_6D6')

    Jump('loc_70F')

    def _loc_6D9(): pass

    label('loc_6D9')

    FadeOut(300, 0, 100)

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
    WaitEffect(0x0F, 0x4A)
    def _loc_70F(): pass

    label('loc_70F')

    Sleep(30)

    TalkEnd(0x00FF)
    ClearMapFlags(0x08000000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
